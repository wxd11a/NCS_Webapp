import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Page,
    Individ_Info,
    Education_Background,
    Post_Grad,
    Individ_PG,
    Base
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    # Pyramid site has it as "if len(argv) != 2;
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        # ori was model = MyModel(name='one', value=1)
        #model = MyModel(name='one', value=1)
        # Douglas, change model = ... to suit the new DB. Possibly with a users table for authentication.
        model = Page(title='Root', body='<p>Root</p>')
        DBSession.add(model)
