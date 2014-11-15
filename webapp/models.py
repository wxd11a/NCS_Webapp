from pyramid.security import Allow, Everyone

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    DateTime
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

# (From Pyramid-blogr) The first line initializes sqlalchemy's threaded session maker - we will use it to interact with [the] database and persist our changes to the databse.
# It is thread-safe meaning that it will handle multipel requests at [the] same time in a safe way, and our code from different views will not impact other requests.
# It will also open and close database connections for us transparently when needed.
# http://pyramid-blogr.readthedocs.org/en/latest/basic_models.html
DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


# Douglas, lookup cryptacular for strong one-way encryption for hashed passwords.
# Douglas, do I want users within .models or .security?
#class User(Base):
#    __tablename__ = 'users'
#    id = Column(Integer, primary_key=True)
#    name = Column(Unicode(255), unique=True, nullable=False)
#    password = Column(unicode(255), nullable=False)
#    last_logged = Column(DateTime, default=datetime.datetime.utcnow)


#class MyModel(Base):
#    __tablename__ = 'models'
#    id = Column(Integer, primary_key=True)
#    name = Column(Text)
#    value = Column(Integer)
#
#Index('my_index', MyModel.name, unique=True, mysql_length=255)

# Page should be a table that holds all the applications with the name associated with each application.
#   It might be better to remove this table since it really is an alias for application_id and the user name
#   The thought behind this is that Page can be queried to list the searched applications instead of having to query Individ_Info
#       for basic information which only iis there to provide a link to the queried application. Doing it this way though would
#       require redundant data, but hopefully would reduce query loads when listing a large amount of applications.
class Page(Base):
    __tablename__ = 'applications'
    uid = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body

class Individ_Info(Base):
    __tablename__ = 'individ_info'

    application_id = Column(Integer, primary_key=True)
    reference = Column(Integer)
    type_professional = Column(Text)
    last_name = Column(Text)
    first_name = Column(Text)
    middle_name = Column(Text)
    suffix_name = Column(Text)
    maiden_name = Column(Text)
    years_associated_one = Column(Text)
    other_name = Column(Text)
    years_associated_two = Column(Text)
    home_mailing_address = Column(Text)
    home_city = Column(Text)
    home_state_or_country = Column(Text)
    home_postal_code = Column(Text)
    home_phone = Column(Text)
    social_security = Column(Text)
    gender = Column(Text)
    correspondence_address = Column(Text)
    correspondence_city = Column(Text)
    correspondence_state_or_country = Column(Text)
    correspondence_postal_code = Column(Text)
    correspondence_phone = Column(Text)
    correspondence_fax = Column(Text)
    correspondence_email = Column(Text)
    dob = Column(Text)
    place_of_birth = Column(Text)
    citizenship = Column(Text)
    visa_number_and_status = Column(Text)
    eligibility = Column(Integer)
    military_service = Column(Integer)
    date_of_service = Column(Text)
    military_last_location = Column(Text)
    military_branch = Column(Text)
    currently_active = Column(Integer)

class Education_Background(Base):
    edu_id = Column(Integer)
    # FOREIGN KEY (edu_id) REFERENCES Individ_Info(application_id)
    professional_degree_institution = Column(Text)
    institution_address = Column(Text)
    institution_city = Column(Text)
    institution_state_or_country = Column(Text)
    institution_postal_code = Column(Text)
    degree = Column(Text)
    attendence_dates(Text)

class Post_Grad(Base):
    post_grad_id = Column(Integer, primary_key=True)
    internship = Column(Integer)
    residency = Column(Integer)
    fellowship = Column(Integer)
    teaching_apt = Column(Integer)
    post_grad_specialty = Column(Text)
    post_grad_institution = Column(Text)
    post_grad_address = Column(Text)
    post_grad_institution_city = Column(Text)
    post_grad_institution_state_or_country = Column(Text)
    post_grad_institution_postal_code = Column(Text)
    post_grad_institution_degree = Column(Text)
    post_grad_institution_completion = Column(Integer)
    post_grad_institution_attendance = Column(Text)
    post_grad_institution_director = Column(Text)
    post_grad_institution_current_director = Column(Text)

#class Individ_Info(Base):
#    __tablename__ = 'individ_info'
##    uid = Column(Integer, 
#    application_id = Column(Integer, primary_key=True)
#    type_professional = Column(Text) # Need to incorporate NOT NULL
#    last_name = Column(Text) # Need to incorporate NOT NULL
#    first_name = Column(Text) # Need to incorporate NOT NULL
#    middle_name = Column(Text) # Need to incorporate NOT NULL
#    suffix_name = Column(Text)
#    maiden_name = Column(Text)
#    years_associated_one = Column(Text) # What does this column mean?
#    other_name = Column(Text) # What does this column mean?
#    years_associated_two = Column(Text) # Need to default to NULL
#    home_mailing_address = Column(Text) # Need to incorporate NOT NULL
#    home_city = Column(Text) # Need to incorporate NOT NULL
#    home_state_or_country = Column(Text) # Need to incorporate NOT NULL
#    home_postal_code = Column(Text) # Need to incorporate NOT NULL
#    home_phone = Column(Text) # Need to incorporate NOT NULL
#    social_security = Column(Text) # Need to incorporate NOT NULL
#    gender = Column(Integer) # Need to incorporate NOT NULL
#    correspondence_address = Column(Text)
#    correspondence_city = Column(Text)
#    correspondence_state_or_country = Column(Text)
#    correspondence_postal_code = Column(Text)
#    correspondence_phone = Column(Text)
#    correspondence_fax = Column(Text)
#    correspondence_email = Column(Text)
#    dob = Column(Text) # Need to incorporate NOT NULL
#    place_of_birth = Column(Text) # Need to incorporate NOT NULL
#    citizenship = Column(Text) # Need to incorporate NOT NULL
#    visa_number_and_status = Column(Text)
#    eligibility = Column(Integer) # Need to incorporate NOT NULL
#    military_service = Column(Integer) # Need to incorporate NOT NULL
#    dates_of_service = Column(Text)
#    military_last_location = Column(Text)
#    military_branch = Column(Text)
#    currently_active = Column(Integer) # Need to incorporate NOT NULL
#
#class Education(Base):
#    __tablename__ = 'education'
#    # id field is for testing since it won't run without a primary key
#    id = Column(Integer, primary_key=True)
#    professional_degree_institution = Column(Text) # NOT NULL
#    institution_address = Column(Text) # Not NULL
#    institution_city = Column(Text) # NOT NULL
#    institution_state_or_country = Column(Text) # Not null
#    institution_postal_code = Column(Text) # NOT NULL
#    degree = Column(Text) # NOT NULL
#    attendence_dates = Column(Text) # NOT NULL
#    extra_degree = Column(Integer)
#    post_grad_edu = Column(Integer)
#    post_grad_specialty = Column(Text)
#    post_grad_institution = Column(Text)
#    post_grad_institution_address = Column(Text)
#    post_grad_institution_city = Column(Text)
#    post_grad_institution_state_or_country = Column(Text)
#    post_grad_institution_postal_code = Column(Text)
#    post_grad_institution_degree = Column(Text)
#    post_grad_institution_completion = Column(Integer)
#    post_grad_institution_attendance = Column(Text)
#    post_grad_institution_director = Column(Text)
#    post_grad_institution_current_director = Column(Text)
#    post_grad_edu_two = Column(Integer)
#    post_grad_specialty_two = Column(Text)
#    post_grad_institution_two = Column(Text)
#    post_grad_institution_two_address = Column(Text)
#    post_grad_institution_two_city = Column(Text)
#    post_grad_institution_two_state_or_country = Column(Text)
#    post_grad_institution_two_postal_code = Column(Text)
#    post_grad_institution_two_degree = Column(Text)
#    post_grad_institution_two_completion = Column(Integer)
#    post_grad_institution_two_attendance = Column(Text)
#    post_grad_institution_two_director = Column(Text)
#    post_grad_institution_two_current_director = Column(Text)
#    post_grad_extra_training = Column(Integer)
#    professional_degree_institution_extra = Column(Text)
#    professional_degree_institution_extra_address = Column(Text)
#    professional_degree_institution_extra_city = Column(Text)
#    professional_degree_institution_extra_state_or_country = Column(Text)
#    professional_degree_institution_extra_postal_code = Column(Text)
#    professional_degree_extra_degree = Column(Text)
#    professional_degree_extra_attendance_dates = Column(Text)
#
#class License_Certificates(Base):
#    __tablename__ = 'license_certificates'
#    # id is for testing since it won't run without a primary key
#    id = Column(Integer, primary_key=True)
#    license_type_one = Column(Text)
#    license_number_one = Column(Text)
#    license_registration_one = Column(Text)
#    license_date_of_issue_one = Column(Text)
#    license_date_of_expiration_one = Column(Text)
#    license_currently_practice_one = Column(Integer)
#    license_type_two = Column(Text)
#    license_number_two = Column(Text)
#    license_registration_two = Column(Text)
#    license_date_of_issue_two = Column(Text)
#    license_date_of_expiration_two = Column(Text)
#    license_currently_practice_two = Column(Integer)
#    license_type_three = Column(Text)
#    license_number_three = Column(Text)
#    license_registraiton_three = Column(Text)
#    license_date_of_issue_three = Column(Text)
#    license_date_of_expiration_three = Column(Text)
#    license_currently_practice_three = Column(Integer)
#    dea_number = Column(Text)
#    dea_date_of_issue = Column(Text)
#    dea_date_of_expiration = Column(Text)
#    dps_number = Column(Text)
#    dps_date_of_issue = Column(Text)
#    dps_date_of_expiration = Column(Text)
#    other_cds = Column(Text)
#    other_cds_number = Column(Text)
#    other_cds_registration = Column(Text)
#    other_cds_date_of_issue = Column(Text)
#    other_cds_date_of_expiration = Column(Text)
#    other_cds_currently_practice = Column(Integer)
#    upin = Column(Text)
#    national_provider = Column(Text)
#    medicare_provider = Column(Integer)
#    medicare_provider_number = Column(Text)
#    medicaid_provider = Column(Integer)
#    medicaid_provider_number = Column(Text)
#    ecfmg = Column(Integer)
#    ecfmg_number = Column(Text)
#    ecfmg_date_of_issue = Column(Text)


class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
                (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass
