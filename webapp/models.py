from pyramid.security import Allow, Everyone

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


#class MyModel(Base):
#    __tablename__ = 'models'
#    id = Column(Integer, primary_key=True)
#    name = Column(Text)
#    value = Column(Integer)
#
#Index('my_index', MyModel.name, unique=True, mysql_length=255)

class Page(Base):
    __tablename__ = 'clientpages'
    uid = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    body = Column(Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body

class Individ_Info(Base):
    __tablename__ = 'Individ_Info'
#    uid = Column(Integer, 
    application_id = Column(Integer, primary_key=True)
    type_professional = Column(Text) # Need to incorporate NOT NULL
    last_name = Column(Text) # Need to incorporate NOT NULL
    first_name = Column(Text) # Need to incorporate NOT NULL
    middle_name = Column(Text) # Need to incorporate NOT NULL
    suffix_name = Column(Text)
    maiden_name = Column(Text)
    years_associated_one = Column(Text) # What does this column mean?
    other_name = Column(Text) # What does this column mean?
    years_associated_two = Column(Text) # Need to default to NULL
    home_mailing_address = Column(Text) # Need to incorporate NOT NULL
    home_city = Column(Text) # Need to incorporate NOT NULL
    home_state_or_country = Column(Text) # Need to incorporate NOT NULL
    home_postal_code = Column(Text) # Need to incorporate NOT NULL
    home_phone = Column(Text) # Need to incorporate NOT NULL
    social_security = Column(Text) # Need to incorporate NOT NULL
    gender = Column(Integer) # Need to incorporate NOT NULL
    correspondence_address = Column(Text)
    correspondence_city = Column(Text)
    correspondence_state_or_country = Column(Text)
    correspondence_postal_code = Column(Text)
    correspondence_phone = Column(Text)
    correspondence_fax = Column(Text)
    correspondence_email = Column(Text)
    dob = Column(Text) # Need to incorporate NOT NULL
    place_of_birth = Column(Text) # Need to incorporate NOT NULL
    citizenship = Column(Text) # Need to incorporate NOT NULL
    visa_number_and_status = Column(Text)
    eligibility = Column(Integer) # Need to incorporate NOT NULL
    military_service = Column(Integer) # Need to incorporate NOT NULL
    dates_of_service = Column(Text)
    military_last_location = Column(Text)
    military_branch = Column(Text)
    currently_active = Column(Integer) # Need to incorporate NOT NULL

# Douglas, ignore this was testing a simple DB call
#pages = {
#    '100': dict(uid='100', title='Page 100', body'<em>100</em>'),
#    '101': dict(uid='101', title='Page 101', body'<em>101</em>'),
#    '102': dict(uid='102', title='Page 102', body'<em>102</em>'),
#}

class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
                (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass
