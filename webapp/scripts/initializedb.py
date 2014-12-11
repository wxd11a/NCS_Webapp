import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

# Douglas, removed Page
from ..models import (
        DBSession,
        User,
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
        IndividPracticeLocationInfo,
        Certs,
        AddOfficeProcedures,
        DisclosureQuestions,
        DisclosureQuestionsExplainations,
        MalpracticeClaims,
        Base
        )



def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    # Pyramid site has it as "if len(argv) != 2;
    # Douglas, was len(argv) < 2
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    # .prepare is used for auto_map
    #Base.prepare(engine, reflect=True)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        # ori was model = MyModel(name='one', value=1)
        #model = MyModel(name='one', value=1)
        # Douglas, change model = ... to suit the new DB. Possibly with a users table for authentication.
        #model = Page(title='Root', body='<p>Root</p>')
        model = IndividInfo(id=int(1), last_name='Cassingham', first_name='Scott', type_professional='anethesiologist')
        # Remember to insert a primary key for all the tables or an AttributeError will occur
        DBSession.add(model)
        model = EducationBackground(id=int(1))
        DBSession.add(model)
        model = PostGrad(id=int(1))
        DBSession.add(model)
        model = LicenseCertificate(id=int(1))
        DBSession.add(model)
        model = LicenseTypes(id=int(1))
        DBSession.add(model)
        model = ProfessionalSpecialtyInfo(id=int(1))
        DBSession.add(model)
        model = WorkHistory(id=int(1))
        DBSession.add(model)
        model = Hospital(id=int(1))
        DBSession.add(model)
        model = ProfessionalLiabilityInsuranceCoverage(id=int(1))
        DBSession.add(model)
        model = CallCoverage(id=int(1))
        DBSession.add(model)
        model = PracticeLocationInfo(id=int(1))
        DBSession.add(model)
        model = Certs(id=int(1))
        DBSession.add(model)
        model = AddOfficeProcedures(id=int(1))
        DBSession.add(model)
        model = DisclosureQuestions(id=int(1))
        DBSession.add(model)
        model = DisclosureQuestionsExplainations(id=int(1))
        DBSession.add(model)
        model = MalpracticeClaims(id=int(1))
        DBSession.add(model)

        # User
        model = User(name='John', password='Doe')
        #transaction.manager.commit()

