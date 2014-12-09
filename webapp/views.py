#import colander
#import deform.widget

from pyramid.decorator import reify
from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import get_renderer
from pyramid.security import remember, forget, authenticated_userid
#from pyramid.response import Response
from pyramid.view import view_config, forbidden_view_config

from sqlalchemy import inspect
from sqlalchemy.exc import DBAPIError

#from .models import (
#    DBSession,
#    MyModel,
#    pages,
#    )

# Douglas, removed Page
from .models import (
        DBSession,
        IndividInfo,
        EducationBackground,
        PostGrad,
        IndividPostGrad,
        LicenseCertificate,
        LicenseTypes,
        IndividLicense,
        ProfessionalSpecialtyInfo,
        WorkHistory,
        Hospital,
        IndividHosp,
        ProfessionalLiabilityInsuranceCoverage,
        CallCoverage,
        PracticeLocationInfo,
        IndividPracticeLoc,
        Certs,
        AddOfficeProcedures,
        DisclosureQuestions,
        DisclosureQuestionsExplainations,
        MalpracticeClaims
        )

from .forms import (
    IndividInfoForm,
    IndividInfoUpdateForm,
    EducationBackgroundForm,
    EducationBackgroundUpdateForm,
    PostGradForm,
    PostGradUpdateForm,
    LicenseCertificateForm,
    LicenseCertificateUpdateForm,
    LicenseTypesForm,
    LicenseTypesUpdateForm,
    ProfessionalSpecialtyInfoForm,
    ProfessionalSpecialtyInfoUpdateForm,
    WorkHistoryForm,
    WorkHistoryUpdateForm,
    HospitalForm,
    HospitalUpdateForm,
    ProfessionalLiabilityInsuranceCoverageForm,
    ProfessionalLiabilityInsuranceCoverageUpdateForm,
    CallCoverageForm,
    CallCoverageUpdateForm,
    PracticeLocationInfoForm,
    PracticeLocationInfoUpdateForm,
    CertsForm,
    CertsUpdateForm,
    AddOfficeProceduresForm,
    AddOfficeProceduresUpdateForm,
    DisclosureQuestionsForm,
    DisclosureQuestionsUpdateForm,
    DisclosureQuestionsExplainationsForm,
    DisclosureQuestionsExplainationsUpdateForm,
    MalpracticeClaimsForm,
    MalpracticeClaimsUpdateForm
    )

from .security import USERS


#@view_config(route_name='home', renderer='templates/mytemplate.pt')
#def my_view(request):
#    try:
#        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
#    except DBAPIError:
#        return Response(conn_err_msg, content_type='text/plain', status_int=500)
#    return {'one': one, 'project': 'webapp'}

#class ClientPage(colander.MappingSchema):
#    title = colander.SchemaNode(colander.String())
#    body = colander.SchemaNode(
#            colander.String(),
#            widget=deform.widget.RichTextWidget()
#    )

class ClientViews(object):
    def __init__(self, request):
        self.request = request
        self.renderer = get_renderer("templates/layout.jinja2")
        #self.uid = ''
        self.full_name = ''
        #self.layout = renderer.implementation().macros['layout']
        #self.logged_in = authenticated_userid(request)
    
    # Douglas, old Colander/Deform form generation
    #@reify
    #def client_form(self):
    #    # Douglas, may need to use ... ClientPage().clone() to create a deep copy so the original schema stays intact
    #    schema = ClientPage()
    #    return deform.Form(schema, buttons=('submit',))

    #@reify
    #def reqts(self):
    #    return self.client_form.get_widget_resources()
    
    # Douglas, this should be the queried list of applications
    @view_config(route_name='client_view',
                renderer='templates/client_view.jinja2')
    def client_view(self):
        #pages = DBSession.query(Page).order_by(Page.title)
        clients = DBSession.query(IndividInfo).order_by(IndividInfo.last_name)
        #return dict(title='Welcome to the Client Page', pages=pages)
        return dict(title='Client List',clients=clients)

    # Douglas, clientpage_add should add a new application
    @view_config(route_name='clientpage_add',
                permission='edit',
                renderer='templates/clientpage_addedit.jinja2')
    def clientpage_add(self):
        # Douglas, may need to pass a var into this so we know the type of form which needs to be created
        
        form = RegistrationForm(self.request.POST)
        if self.request.method == 'POST' and form.validate():
            client = IndividInfo()
            #user.username = form.username.data
            #user.email = form.email.data
            #user.save()
            #redirect('register')

        return self.renderer('clientpage_addedit', form=form)


        # Douglas, previous form call
        #form = self.client_form.render()
        
        # Douglas, old Colander/Deform forms
        #if 'submit' in self.request.params:
        #    controls = self.request.POST.items()
        #    try:
        #        appstruct = self.client_form.validate(controls)
        #    except deform.ValidationFailure as e:
        #        # Form is NOT valid
        #        return dict(title='Add Client Page', form=e.render())

        #    # Add a new page to the DB
        #    new_title = appstruct['title']
        #    new_body = appstruct['body']
        #    DBSession.add(Page(new_title, new_body))

        #    # Get the new ID and redirect
        #    page = DBSession.query(Page).filter_by(title=new_title).one()
        #    new_uid = page.uid

        #    # Now visit new page
        #    url = self.request.route_url('clientpage_view', uid=new_uid)
        #    return HTTPFound(url)

        #return dict(title='Add Client Page', form=self.client_form.render())
    
    # Douglas, this should be the standard view for applications. Ideally there would be a link to edit which would lead to an edit view
    @view_config(route_name='clientpage_view',
                renderer='templates/clientpage_view.jinja2')
    def clientpage_view(self):

        # Retrieving the uid (aka IndividInfo.id) as selected by the link from the previous page
        id = self.request.matchdict['uid']
        # Get the selected navigation view (ex. Individual Information, Education, etc.)
        loc = self.request.matchdict['loc']

	# Individual's Information
	# Education Background
	# Professional Information
	# Work History
	# Hospital Affiliations
	# References
	# Insurance Coverage
	# Call Coverage
	# Practice Location Information
	# Disclosure Questions
	# Standard Authorization, Attestation, and Release

        # Match the query with the location. Using if/elif is ugly as hell. Find a better way -  Dicitonary perhaps?
        #client = DBSession.query(IndividInfo).filter_by(id=id).one()

        # Query with first() as not to return an error if information is missing
        if loc == 'individual':
            client = DBSession.query(IndividInfo).filter_by(id=id).first()
            full_name = "{}, {}".format(client.last_name, client.first_name)
            self.full_name = full_name
            form = IndividInfoUpdateForm(self.request.POST)
        elif loc == 'education':
            client = DBSession.query(EducationBackground).filter_by(id=id).first()
            form = EducationBackgroundUpdateForm(self.request.POST)
        elif loc == 'professional':
            client = DBSession.query(ProfessionalSpecialtyInfo).filter_by(id=id).first()
            form = ProfessionalSpecialtyInfoUpdateForm(self.request.POST)
        elif loc == 'history':
            client = DBSession.query(WorkHistory).filter_by(id=id).first()
            form = WorkHistoryUpdateForm(self.request.POST)
        elif loc == 'affiliations':
            client = DBSession.query(Hospital).filter_by(id=id).first()
            form = HospitalUpdateForm(self.request.POST)
        elif loc == 'references':
            client = DBSession.query(IndividInfo).filter_by(id=id).first()
            form = IndividInfoUpdateForm(self.request.POST)
        elif loc == 'insurancecoverage':
            client = DBSession.query(ProfessionalLiabilityInsuranceCoverage).filter_by(id=id).first()
            form = ProfessionalLiabilityInsuraceCoverageUpdateForm(self.request.POST)
        elif loc == 'callcoverage':
            client = DBSession.query(CallCoverage).filter_by(id=id).first()
            form = CallCoverageUpdateForm(self.request.POST)
        elif loc == 'location':
            client = DBSession.query(PracticeLocationInfo).filter_by(id=id).first()
            form = PracticeLocationInfoUpdateForm(self.request.POST)
        elif loc == 'disclosure':
            client = DBSession.query(DisclosureQuestions).filter_by(id=id).first()
            form = DisclosureQuestionsUpdateForm(self.request.POST)
        elif loc == 'standards':
            client = DBSession.query(MalpracticeClaims).filter_by(id=id).first()
            form = MalpracticeClaimsUpdateForm(self.request.POST)
        #if loc == 'individual':
        #    client = DBSession.query(IndividInfo).filter_by(id=id).one()
        #    # Creating a full_name from the currently selected practitioner and assigning it to title in the dict()
        #    full_name = "{}, {}".format(client.last_name, client.first_name)
        #    self.full_name = full_name
        #elif loc == 'education':
        #    client = DBSession.query(EducationBackground).filter_by(id=id).first()
        #elif loc == 'professional':
        #    client = DBSession.query(ProfessionalSpecialtyInfo).filter_by(id=id).one()
        #elif loc == 'history':
        #    client = DBSession.query(WorkHistory).filter_by(id=id).one()
        #elif loc == 'affiliations':
        #    client = DBSession.query(Hospital).filter_by(id=id).one()
        #elif loc == 'references':
        #    client = DBSession.query(IndividInfo).filter_by(id=id).one()
        #elif loc == 'insurancecoverage':
        #    client = DBSession.query(ProfessionalLiabilityInsuranceCoverage).filter_by(id=id).one()
        #elif loc == 'callcoverage':
        #    client = DBSession.query(CallCoverage).filter_by(id=id).one()
        #elif loc == 'location':
        #    client = DBSession.query(PracticeLocationInfo).filter_by(id=id).one()
        #elif loc == 'disclosure':
        #    client = DBSession.query(DisclosureQuestions).filter_by(id=id).one()
        #elif loc == 'standards':
        #    client = DBSession.query(MalpracticeClaims).filter_by(id=id).one()


        # Getting the alternative name for use in printing
        #mapper = inspect(client)
        #docs = []
        #for column in mapper.attrs:
        #    docs.append(column.key)

        if self.request.method == 'POST' and form.validate():
            form.populate_obj(client)
        # Douglas, added form=form since wtforms-alchemy generates the page in a less error prone way
        return dict(client=client,form=form, title=self.full_name, uid=id, loc=loc)
    
    # Douglas, this should be an existing application page
    # Douglas, removed permission='edit'
    @view_config(route_name='clientpage_edit',
                renderer='templates/clientpage_addedit.jinja2')
    def clientpage_edit(self):
        #uid = int(self.request.matchdict['uid'])
        # page = DBSession.query(Page).filter_by(uid=uid).one()
        #title = 'Edit ' + page.title
        
        # Get the user id of the practitioner, the section to edit, and query for data pertaining to the user
        id = self.request.matchdict['uid']
        loc = self.request.matchdict['loc']

        # Query with first() as not to return an error if information is missing
        if loc == 'individual':
            client = DBSession.query(IndividInfo).filter_by(id=id).first()
            form = IndividInfoUpdateForm(self.request.POST)
        elif loc == 'education':
            client = DBSession.query(EducationBackground).filter_by(id=id).first()
            form = EducationBackgroundUpdateForm(self.request.POST)
        elif loc == 'professional':
            client = DBSession.query(ProfessionalSpecialtyInfo).filter_by(id=id).first()
            form = ProfessionalSpecialtyInfoUpdateForm(self.request.POST)
        elif loc == 'history':
            client = DBSession.query(WorkHistory).filter_by(id=id).first()
            form = WorkHistoryUpdateForm(self.request.POST)
        elif loc == 'affiliations':
            client = DBSession.query(Hospital).filter_by(id=id).first()
            form = HospitalUpdateForm(self.request.POST)
        elif loc == 'references':
            client = DBSession.query(IndividInfo).filter_by(id=id).first()
            form = IndividInfoUpdateForm(self.request.POST)
        elif loc == 'insurancecoverage':
            client = DBSession.query(ProfessionalLiabilityInsuranceCoverage).filter_by(id=id).first()
            form = ProfessionalLiabilityInsuraceCoverageUpdateForm(self.request.POST)
        elif loc == 'callcoverage':
            client = DBSession.query(CallCoverage).filter_by(id=id).first()
            form = CallCoverageUpdateForm(self.request.POST)
        elif loc == 'location':
            client = DBSession.query(PracticeLocationInfo).filter_by(id=id).first()
            form = PracticeLocationInfoUpdateForm(self.request.POST)
        elif loc == 'disclosure':
            client = DBSession.query(DisclosureQuestions).filter_by(id=id).first()
            form = DisclosureQuestionsUpdateForm(self.request.POST)
        elif loc == 'standards':
            client = DBSession.query(MalpracticeClaims).filter_by(id=id).first()
            form = MalpracticeClaimsUpdateForm(self.request.POST)

        # WTForms
        #form = ProfileForm(request,POST,id)  
        
        if self.request.method == 'POST' and form.validate():
            form.populate_obj(client)
            # Add the changes to the DBSession
            DBSession.add(client)
            DBSession.commit()
            
            # Example using Flask
            #redirect('clientpage_edit')
            
            # Douglas, not sure about this url response with a render_reponse
            url = self.request.route_url('clientpage_view', uid=id)
            return HTTPFound(url)

        
        return dict(client=client, form=form, uid=id)
            
        
        # Douglas, old Colander/Deform forms
        #if 'submit' in self.request.params:
        #    controls = self.request.POST.items()
        #    try:
        #        appstruct = self.client_form.validate(controls)
        #    except deform.ValidationFailure as e:
        #        return dict(title=title, page=page, form=e.render())

        #    # Change the content and redirect to the view
        #    page.title = appstruct['title']
        #    page.body = appstruct['body']

        #    url = self.request.route_url('clientpage_view', uid=uid)
        #    return HTTPFound(url)

        #form = self.client_form.render(dict(uid=page.uid, title=page.title, body=page.body))

        #return dict(page=page, title=title, form=form)

    @view_config(route_name='clientpage_delete', permission='edit')
    def clientpage_delete(self):
        uid = int(self.request.matchdict['uid'])
        page = DBSession.query(Page).filter_by(uid=uid).one()
        DBSession.delte(page)

        url = self.request.route_url('client_view')
        return HTTPFound(url)

    @view_config(route_name='login', renderer='templates/login.jinja2')
    @forbidden_view_config(renderer='templates/login.jinja2')
    def login(self):
        request = self.request
        login_url = request.route_url('login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/' # never use login form itself as came_from
        came_from = request.params.get('came_from', referrer)
        message = ''
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            if USERS.get(login) == password:
                headers = remember(request, login)
                return HTTPFound(location=came_from, headers=headers)
            message = 'Failed login'

        return dict(
                title='Login',
                message=message,
                url=request.application_url + '/login',
                came_from=came_from,
                login=login,
                password=password,
                )

    @view_config(route_name='logout')
    def logout(self):
        request = self.request
        headers = forget(request)
        url = request.route_url('client_view')
        return HTTPFound(location=url,
                        headers=headers)

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_webapp_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

