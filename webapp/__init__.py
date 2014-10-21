from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from .models import DBSession, Base

from .security import groupfinder

#from .models import (
#    DBSession,
#    Base,
#    )
#

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings,
                            root_factory='webapp.models.Root')
    config.include('pyramid_chameleon')
    
    # Security policies
    authn_policy = AuthTktAuthenticationPolicy(
            'sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy() 
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.add_route('client_view', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('clientpage_add', '/add')
    config.add_route('clientpage_view', '/{uid}')
    config.add_route('clientpage_edit', '/{uid}/edit')
    config.add_route('clientpage_delete', '/{uid}/delete')
    config.add_static_view(name='static', path='webapp:static', cache_max_age=3600)
    config.add_static_view('deform_static', 'deform:static/')

    config.scan()
    return config.make_wsgi_app()
