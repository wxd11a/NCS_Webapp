import colander
import deform.widget

from pyramid.decorator import reify
from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import get_renderer
from pyramid.security import remember, forget, authenticated_userid
#from pyramid.response import Response
from pyramid.view import view_config, forbidden_view_config

from sqlalchemy.exc import DBAPIError

#from .models import (
#    DBSession,
#    MyModel,
#    pages,
#    )

from .models import DBSession, Individ_Info, Education, Licence_Certificates
from .security import USERS


#@view_config(route_name='home', renderer='templates/mytemplate.pt')
#def my_view(request):
#    try:
#        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
#    except DBAPIError:
#        return Response(conn_err_msg, content_type='text/plain', status_int=500)
#    return {'one': one, 'project': 'webapp'}

class ClientPage(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())
    body = colander.SchemaNode(
            colander.String(),
            widget=deform.widget.RichTextWidget()
    )

class ClientViews(object):
    def __init__(self, request):
        self.request = request
        renderer = get_renderer("templates/layout.pt")
        self.layout = renderer.implementation().macros['layout']
        self.logged_in = authenticated_userid(request)

    @reify
    def client_form(self):
        schema = ClientPage()
        return deform.Form(schema, buttons=('submit',))

    @reify
    def reqts(self):
        return self.client_form.get_widget_resources()

    # Will also need a Practitioner view
    @view_config(route_name='client_view',
                renderer='templates/client_view.pt')
    def client_view(self):
        pages = DBSession.query(Page).order_by(Page.title)
        return dict(title='Welcome to the Client Page', pages=pages)

    @view_config(route_name='clientpage_add',
                permission='edit',
                renderer='templates/clientpage_addedit.pt')
    def clientpage_add(self):
        # Douglas, previous form call
        #form = self.client_form.render()

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.client_form.validate(controls)
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict(title='Add Client Page', form=e.render())

            # Add a new page to the DB
            new_title = appstruct['title']
            new_body = appstruct['body']
            DBSession.add(Page(new_title, new_body))

            # Get the new ID and redirect
            page = DBSession.query(Page).filter_by(title=new_title).one()
            new_uid = page.uid

            # Now visit new page
            url = self.request.route_url('clientpage_view', uid=new_uid)
            return HTTPFound(url)

        return dict(title='Add Client Page', form=self.client_form.render())

    @view_config(route_name='clientpage_view',
                renderer='templates/clientpage_view.pt')
    def clientpage_view(self):
        uid = self.request.matchdict['uid']
        page = DBSession.query(Page).filter_by(uid=uid).one()

        return dict(page=page, title=page['title'])

    @view_config(route_name='clientpage_edit',
                permission='edit',
                renderer='templates/clientpage_addedit.pt')
    def clientpage_edit(self):
        uid = int(self.request.matchdict['uid'])
        page = DBSession.query(Page).filter_by(uid=uid).one()
        title = 'Edit ' + page.title

#        client_form = self.client_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.client_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(title=title, page=page, form=e.render())

            # Change the content and redirect to the view
            page.title = appstruct['title']
            page.body = appstruct['body']

            url = self.request.route_url('clientpage_view', uid=uid)
            return HTTPFound(url)

        form = self.client_form.render(dict(uid=page.uid, title=page.title, body=page.body))

        return dict(page=page, title=title, form=form)

    @view_config(route_name='clientpage_delete', permission='edit')
    def clientpage_delete(self):
        uid = int(self.request.matchdict['uid'])
        page = DBSession.query(Page).filter_by(uid=uid).one()
        DBSession.delte(page)

        url = self.request.route_url('client_view')
        return HTTPFound(url)

    @view_config(route_name='login', renderer='templates/login.pt')
    @forbidden_view_config(renderer='templates/login.pt')
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

