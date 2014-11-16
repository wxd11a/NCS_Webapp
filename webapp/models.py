from pyramid.security import Allow, Everyone

from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    DateTime
    )

from sqlalchemy.orm import relationship, backref
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
#class Page(Base):
#    __tablename__ = 'applications'
#    uid = Column(Integer, primary_key=True)
#    title = Column(Text)
#    body = Column(Text)
#
#    def __init__(self, title, body):
#        self.title = title
#        self.body = body

class Individ_Info(Base):
    __tablename__ = 'individ_info'
    
    # Changed application_id to id because it is too verbose and can be identified by its class when called
    id = Column(Integer, primary_key=True)
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
    # for association between tables
    # Douglas, commented out while testing without 3NF
    #children = relationship('individ_pg')

class Education_Background(Base):
    __tablename__ = 'education_background'

    # Douglas, added the id since edu_id is the FK. Changed edu_id to app_id since that is what it references
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, ForeignKey('individ_info.id'))
    # FOREIGN KEY (edu_id) REFERENCES Individ_Info(application_id)
    professional_degree_institution = Column(Text)
    institution_address = Column(Text)
    institution_city = Column(Text)
    institution_state_or_country = Column(Text)
    institution_postal_code = Column(Text)
    degree = Column(Text)
    attendance_dates = Column(Text)

class Post_Grad(Base):
    __tablename__ = 'post_grad'
    
    # Douglas, changed post_grad_id to id because it will be recognized as post_grad.id when called
    id = Column(Integer, primary_key=True)
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

#class Individ_PG(Base):
#    __tablename__ = 'individ_pg'
#
#    ind_id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
#    pg_id = Column(Integer, ForeignKey('post_grad.id'), primary_key=True)
    # FOREIGN KEY (Ind_ID) REFERENCES Individ_Info(application_id)
    # FOREIGN KEY (PG_ID) REFERENCES Post_Grad(post_grad_id)



class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
                (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass
