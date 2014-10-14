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

# Douglas, ignore this was testing a simple DB call
#pages = {
#    '100': dict(uid='100', title='Page 100', body'<em>100</em>'),
#    '101': dict(uid='101', title='Page 101', body'<em>101</em>'),
#    '102': dict(uid='102', title='Page 102', body'<em>102</em>'),
#}

class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
                (allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass
