from pyramid.security import (
        Everyone,
        Authenticated,
        Allow,
        )

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

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from wtforms_alchemy import ModelForm

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

class IndividInfo(Base):
    __tablename__ = 'individ_info'
    
    # Changed application_id to id because it is too verbose and can be identified by its class when called
    id = Column(Integer, primary_key=True)
    last_name = Column(Text, key='Last name')
    first_name = Column('First name',Text, key='First name')
    reference = Column(Integer, key='Reference')
    type_professional = Column(Text, key='Type')
    middle_name = Column(Text, key='Middle name')
    suffix_name = Column(Text, key='Suffix')
    maiden_name = Column(Text, key='Maiden name')
    years_associated_one = Column(Text, key='Years Associated One')
    other_name = Column(Text, key='Other name')
    years_associated_two = Column(Text, key='Years associated Two')
    home_mailing_address = Column(Text, key='Home Mailing Address')
    home_city = Column(Text, key='Home city')
    home_state_or_country = Column(Text, key='Home state or country')
    home_postal_code = Column(Text, key='Home Postal code')
    home_phone = Column(Text, key='Home phone')
    social_security = Column(Text, key='Social Security Number')
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

    # for association between association table and post_grad
    post_grads = association_proxy('individ_pgs', 'post_grad')

    # for association between assoc table and pratice_loc
    practice_locs = association_proxy('individ_practicelocs', 'practice_loc')

    # for association between assoc table and hospital
    hospitals = association_proxy('individ_hosps', 'hospital')



    #@classmethod
    #def _get_keys(cls):
    #    return sa.orm.class_mapper(cls).c.keys()

    #def get_dict(self):
    #    d = {}
    #    for k in self._get_keys():
    #        d[k] = getattr(self, k)
    #    return d


class EducationBackground(Base):
    __tablename__ = 'education_background'

    # Douglas, added the id since edu_id is the FK. Changed edu_id to app_id since that is what it references
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, ForeignKey('individ_info.id'))
    professional_degree_institution = Column(Text)
    institution_address = Column(Text)
    institution_city = Column(Text)
    institution_state_or_country = Column(Text)
    institution_postal_code = Column(Text)
    degree = Column(Text)
    attendance_dates = Column(Text)

class PostGrad(Base):
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

# Association table
class IndividPostGrad(Base):
    __tablename__ = 'individ_pg'

    ind_id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
    pg_id = Column(Integer, ForeignKey('post_grad.id'), primary_key=True)

    # bidirecitonal attribute/collection of individ_info/individ_pg
    individ_info = relationship(IndividInfo,
                        backref=backref("individ_pgs",
                            cascade="all, delete-orphan")
                        )

    # reference to Post_Grad object
    post_grad = relationship("PostGrad")

class LicenseCertificates:
    __tablename__ = 'license_certificates'

    id = Column(Integer, primary_key=True)
    dea_number = Column(Text)
    dea_date_of_issue = Column(Text)
    dea_date_of_expiration = Column(Text)
    dps_number = Column(Text)
    dps_date_of_issue = Column(Text)
    dps_date_of_expiration = Column(Text)
    other_cds = Column(Text)
    other_cds_number = Column(Text)
    other_cds_registration = Column(Text)
    other_cds_date_of_issue = Column(Text)
    other_cds_date_of_expiration = Column(Text)
    other_cds_currently_practice = Column(Integer)
    upin = Column(Text)
    national_provider = Column(Text)
    medicare_provider = Column(Integer)
    medicare_provider_number = Column(Text)
    medicaid_provider = Column(Integer)
    medicaid_provider_number = Column(Text)
    ecfmg = Column(Integer)
    ecfmg_number = Column(Text)
    ecfmg_date_of_issue = Column(Text)

class LicenseTypes:
    __tablename__ = 'license_types'

    id = Column(Integer, ForeignKey('license_certificates.id'), primary_key=True)
    license_type = Column(Text)
    license_number = Column(Text)
    license_registration = Column(Text)
    license_date_of_issue = Column(Text)
    license_date_of_expiration = Column(Text)
    license_currently_practice = Column(Integer)
    # FOREIGN KEY (lic_cert_id) REFERENCES License_Certificates(license_id)

# Association table
class IndividLicense:
    __tablename__ = 'individ_license'

    l_id = Column(Integer, ForeignKey('license_certificates.id'), primary_key=True)
    i_id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
    # FOREIGN KEY (L_ID) REFERENCES LicenseCertificates(license_id)
    # FOREIGN KEY (I_ID) REFERENCES IndividInfo(application_id)

class ProfessionalSpecialtyInfo:
    __tablename__ = 'professional_specialty_info'

    id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
    primary_specialty = Column(Integer)
    specialty = Column(Text)
    board_certified = Column(Integer)
    board_name = Column(Text)
    initial_certification_date = Column(Text)
    recertification_date = Column(Text)
    certification_expiration_date = Column(Text)
    board_certification_exam = Column(Integer)
    board_certification_board  = Column(Text)
    board_certification_part_II = Column(Integer)
    board_certification_exam_name = Column(Text)
    board_certification_sit = Column(Integer)
    board_certification_sit_date = Column(Text)
    board_certification_no_board = Column(Integer)
    directory_listed_hmo = Column(Integer)
    directory_listed_ppo = Column(Integer)
    directory_listed_pos = Column(Integer)
    other_areas_professional_practice = Column(Text)

class WorkHistory:
    __tablename__ = 'work_history'

    id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
    current_practice = Column(Integer)
    practice_name = Column(Text)
    start_date = Column(Text)
    end_date = Column(Text)
    practice_address = Column(Text)
    practice_city = Column(Text)
    practice_state_or_country = Column(Text)
    practice_postal_code = Column(Text)
    practice_reason_for_discontinuance = Column(Text)

class Hospital:
    __tablename__ = 'hospital'

    id = Column(Integer, primary_key=True)
    hospital_primary = Column(Integer)
    hospital_privileges = Column(Integer)
    admitting_arrangements = Column(Text)
    hospital = Column(Text)
    hospital_start_date = Column(Text)
    hospital_end_date = Column(Text)
    hospital_address = Column(Text)
    hospital_city = Column(Text)
    hospital_state_or_country = Column(Text)
    hospital_postal_code = Column(Text)
    hospital_phone = Column(Text)
    hospital_fax = Column(Text)
    hospital_email = Column(Text)
    hospital_unrestricted_privileges = Column(Integer)
    hospital_types_of_privileges = Column(Text)
    hospital_temporary_privileges = Column(Integer)
    hospital_admission_percentage = Column(Text)
    hospital_reason_for_leaving = Column(Text)

# Association table
class IndividHosp:
    __tablename__ = 'individ_hosp'

    H_id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
    I_id = Column(Integer, ForeignKey('hospital.id'), primary_key=True)

    # bidirectional attribute/collection of individ_info/individ_hosps
    individ_info = relationship(IndividInfo,
                        backref=backref("individ_hosps",
                            cascade="all, delete-orphan")
                        )

    # reference to the Hospital object
    hospital = relationship("Hospital")

class ProfessionalLiabilityInsuranceCoverage:
    __tablename__ = 'professional_liability_insurance_coverage'

    id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
    self_insured = Column(Integer)
    malpractice_insurance_name = Column(Text)
    malpractice_insurance_address = Column(Text)
    malpractice_insurance_city = Column(Text)
    malpractice_insurance_state_or_country = Column(Text)
    malpractice_insurance_postal_code = Column(Text)
    malpractice_insurance_phone = Column(Text)
    malpractice_insurance_policy_number = Column(Text)
    malpractice_insurance_effective_date = Column(Text)
    malpractice_insurance_expiration_date = Column(Text)
    malpractice_insurance_coverage_per_occurence = Column(Text)
    malpractice_insurance_coverage_aggregate = Column(Text)
    malpractice_insurance_coverage_type = Column(Integer)
    malpractice_insurance_time_with_carrier = Column(Text)

class CallCoverage:
    __tablename__ = 'call_coverage'

    id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
    colleague_name = Column(Text)
    colleague_specialty = Column(Text)
    practice_partners_name = Column(Text)

class PracticeLocationInfo:
    __tablename__ = 'practice_location_info'

    id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
    practice_location_name = Column(Text)
    service_type = Column(Integer)
    practice_name_in_directory = Column(Text)
    practice_name_in_w9 = Column(Text)
    practice_location_primary = Column(Integer)
    practice_address = Column(Text)
    practice_city = Column(Text)
    practice_state_or_country = Column(Text)
    practice_postal_code = Column(Text)
    practice_phone = Column(Text)
    practice_fax = Column(Text)
    practice_email = Column(Text)
    practice_backoffice_phone = Column(Text)
    practice_medicaid_number = Column(Text)
    practice_tax_id_number = Column(Text)
    practice_tax_number = Column(Text)
    practice_tax_name = Column(Text)
    currently_practicing = Column(Integer)
    practice_expected_state_date = Column(Text)
    practice_list_in_directory = Column(Integer)
    practice_manager = Column(Text)
    practice_manager_phone = Column(Text)
    practice_manager_fax = Column(Text)
    credentialing_contact = Column(Text)
    credentialing_contact_address = Column(Text)
    credentialing_contact_city = Column(Text)
    credentialing_contact_state_or_country = Column(Text)
    credentialing_contact_postal_code = Column(Text)
    billing_company_name = Column(Text)
    billing_company_representative = Column(Text)
    billing_representative_address = Column(Text)
    billing_representative_city = Column(Text)
    billing_representative_state_or_country = Column(Text)
    billing_representative_postal_code = Column(Text)
    billing_representative_phone = Column(Text)
    billing_representative_fax = Column(Text)
    billing_representative_email = Column(Text)
    billing_representative_dept_name = Column(Text)
    billing_representative_check_payable_to = Column(Text)
    billing_representative_electronic_bill = Column(Text)
    hours_seen_monday_available = Column(Integer)
    hours_seen_monday_morning = Column(Text)
    hours_seen_monday_afternoon = Column(Text)
    hours_seen_monday_evening = Column(Text)
    hours_seen_tuesday_available = Column(Integer)
    hours_seen_tuesday_morning = Column(Text)
    hours_seen_tuesday_afternoon = Column(Text)
    hours_seen_tuesday_evening = Column(Text)
    hours_seen_wednesday_available = Column(Integer)
    hours_seen_wednesday_morning = Column(Text)
    hours_seen_wednesday_afternoon = Column(Text)
    hours_seen_wednesday_evening = Column(Text)
    hours_seen_thursday_available = Column(Integer)
    hours_seen_thursday_morning = Column(Text)
    hours_seen_thursday_afternoon = Column(Text)
    hours_seen_thursday_evening = Column(Text)
    hours_seen_friday_available = Column(Integer)
    hours_seen_friday_morning = Column(Text)
    hours_seen_friday_afternoon = Column(Text)
    hours_seen_friday_evening = Column(Text)
    hours_seen_saturday_available = Column(Integer)
    hours_seen_saturday_morning = Column(Text)
    hours_seen_saturday_afternoon = Column(Text)
    hours_seen_saturday_evening = Column(Text)
    hours_seen_sunday_available = Column(Integer)
    hours_seen_sunday_morning = Column(Text)
    hours_seen_sunday_afternoon = Column(Text)
    hours_seen_sunday_evening = Column(Text)
    practice_24_7_phone_coverage = Column(Integer)
    practice_accepts = Column(Integer)
    new_patient_acceptance_variation = Column(Text)
    practice_limitations_gender = Column(Integer)
    practice_limitations_age = Column(Text)
    practice_limitations_other = Column(Text)
    other_care_providers = Column(Integer)
    other_care_providers_name_one = Column(Text)
    other_care_providers_professional_designation_one = Column(Text)
    other_care_providers_providers_state_one = Column(Text)
    other_care_providers_license_one = Column(Text)
    other_care_providers_name_two = Column(Text)
    other_care_providers_professional_designation_two = Column(Text)
    other_care_providers_state_two = Column(Text)
    other_care_providers_license_two = Column(Text)
    other_care_providers_name_three = Column(Text)
    other_care_providers_professional_designation_three = Column(Text)
    other_care_providers_state_three = Column(Text)
    other_care_providers_license_three = Column(Text)
    other_care_providers_name_four = Column(Text)
    other_care_providers_professional_designation_four = Column(Text)
    other_care_providers_providers_state_four = Column(Text)
    other_care_providers_license_four = Column(Text)
    other_care_providers_name_five = Column(Text)
    other_care_providers_professional_designation_five = Column(Text)
    other_care_providers_providers_state_five = Column(Text)
    other_care_providers_license_five = Column(Text)
    other_care_providers_name_six = Column(Text)
    other_care_providers_professional_designation_six = Column(Text)
    other_care_providers_providers_state_six = Column(Text)
    other_care_providers_license_six = Column(Text)
    health_care_provider_non_english_lang = Column(Text)
    office_personnel_non_english_lang = Column(Text)
    interpreter_available_bool = Column(Integer)
    interpreter_available_lang = Column(Text)
    practice_ada_accessibility = Column(Integer)
    handicap_accessible_facility = Column(Integer)
    handicap_accessible_facility_other = Column(Text)
    disable_services = Column(Integer)
    disable_services_other = Column(Text)
    practice_public_transportation = Column(Integer)
    practice_public_transportation_other = Column(Text)
    practice_childcare_services = Column(Integer)
    practice_minority_b_e = Column(Integer)
    basic_life_support_cert_staff = Column(Integer)
    basic_life_support_cert_exp_date = Column(Text)
    advanced_life_support_ob_staff = Column(Integer)
    advanced_life_support_ob_exp_date = Column(Text)
    advanced_trauma_support_staff = Column(Integer)
    advanced_trauma_support_exp_date = Column(Text)
    cardio_pulmonary_resucitation_staff = Column(Integer)
    cardio_pulmonary_resucitation_exp_date = Column(Text)
    adv_cardiac_life_support_staff = Column(Integer)
    adv_cardiac_life_support_exp_date = Column(Text)
    pediatric_adv_life_support_staff = Column(Integer)
    pediatric_adv_life_support_exp_date = Column(Text)
    neonatal_adv_life_support_staff = Column(Integer)
    neonatal_adv_life_support_exp_date = Column(Text)
    other_current_cert = Column(Text)
    other_current_cert_staff = Column(Integer)
    other_current_cert_exp_date = Column(Text)
    practice_service_on_site = Column(Integer)
    lab_services = Column(Integer)
    radiology_services = Column(Integer)
    allergy_injections = Column(Integer)
    age_appropriate_immunizations = Column(Integer)
    osteopathic_manipulation = Column(Integer)
    ekg = Column(Integer)
    allergy_skin_treatments = Column(Integer)
    flexible_sigmoidoscopy = Column(Integer)
    iv_hydration = Column(Integer)
    care_of_minor_lacerations = Column(Integer)
    routine_office_gynecology = Column(Integer)
    tympanometry_auiometry_test = Column(Integer)
    cardiac_stress_test = Column(Integer)
    pulmonary_function_test = Column(Integer)
    drawing_blood = Column(Integer)
    asthma_treatment = Column(Integer)
    physical_therapies = Column(Integer)
    other_services = Column(Integer)
    other_services_list = Column(Text)
    anasthesia_administered = Column(Integer)
    anasthesia_administered_categories = Column(Text)
    anasthesia_administrator = Column(Text)

# Association table
class IndividPracticeLoc:
    __tablename__ = 'individ_practice_loc'

    I_id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
    Lo_id = Column(Integer, ForeignKey('practice_location_info.id'), primary_key=True)

    # bidirecitonal attribute/collection of individ_info/individ_practicelocs
    individ_info = relationship(IndividInfo,
                        backref=backref("individ_practicelocs",
                            cascade="all, delete-orphan")
                        )

    # reference to the PracticeLoc object
    practice_loc = relationship("PracticeLoc")

class Certs:
    __tablename__ = 'certs'

    id = Column(Integer, ForeignKey('location.id'), primary_key=True)
    name = Column(Text)
    type = Column(Text)

class AddOfficeProcedures:
    __tablename__ = 'add_office_procedures'

    id = Column(Integer, ForeignKey('practice_location_info.id'), primary_key=True)
    description = Column(Text)

class DisclosureQuestions:
    __tablename__ = 'disclosure_questions'
    
    # Douglas, should id also be a primary key since it is a fk to individ_id?
    id = Column(Integer, ForeignKey('individ_info.id'))
    question_number = Column(Integer, primary_key=True)
    question_answer = Column(Integer)

class DisclosureQuestionsExplainations:
    __tablename__ = 'disclosure_questions_explainations'
    # Douglas, should I just name explaination_number to id to be consistent? Probably.
    explaination_number = Column(Integer, ForeignKey('disclosure_questions.question_number', primary_key=True))
    question_explaination = Column(Text)

class MalpracticeClaims:
    __tablename__ = 'malpractice_claims'

    id = Column(Integer, ForeignKey('individ_info.id'), primary_key=True)
    incident_date = Column(Text)
    date_filed = Column(Text)
    claim_status = Column(Text)
    carrier_involved = Column(Text)
    carrier_address = Column(Text)
    carrier_city = Column(Text)
    carrier_state_or_country = Column(Text)
    carrier_postal_code = Column(Text)
    carrier_phone = Column(Text)
    carrier_polity_number = Column(Text)
    settlement = Column(Text)
    paid = Column(Text)
    resolution = Column(Integer)
    description = Column(Text)
    defendant = Column(Text)
    co_defendant = Column(Integer)
    involvement = Column(Text)
    injury_to_patient = Column(Text)
    npdb = Column(Integer)

class Root(object):
    # Douglas, ... (Allow, 'group:editors', 'edit')]
    # .... (Allow, Authenticated, 'edit')
    __acl__ = [(Allow, Everyone, 'view'),
            (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass
