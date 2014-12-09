from wtforms_alchemy import ModelForm#, ModelFieldList
from wtforms.fields import FormField
from wtforms_components import DateField
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
        IndividPracticeLocationInfo,
        Certs,
        AddOfficeProcedures,
        DisclosureQuestions,
        DisclosureQuestionsExplainations,
        MalpracticeClaims
        )

# WTF-Alchemy ties its form schema to the SQLAlchemy model schema. This makes form generation manageable.

# Douglas, possibly could generate labels here to avoid autoescaping the html
class IndividInfoForm(ModelForm):
    class Meta:
        model = IndividInfo
    
    @classmethod
    def get_session(self):
        return self.DBSession

# An update class for Individ_Info so not all the vields need to be validated
class IndividInfoUpdateForm(IndividInfoForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class EducationBackgroundForm(ModelForm):
    class Meta:
        model = EducationBackground

class EducationBackgroundUpdateForm(EducationBackgroundForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class PostGradForm(ModelForm):
    class Meta:
        model = PostGrad

class PostGradUpdateForm(PostGradForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class LicenseCertificateForm(ModelForm):
    class Meta:
        model = LicenseCertificate

class LicenseCertificateUpdateForm(LicenseCertificateForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class LicenseTypesForm(ModelForm):
    class Meta:
        model = LicenseTypes

class LicenseTypesUpdateForm(LicenseTypesForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class ProfessionalSpecialtyInfoForm(ModelForm):
    class Meta:
        model = ProfessionalSpecialtyInfo

class ProfessionalSpecialtyInfoUpdateForm(ProfessionalSpecialtyInfoForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class WorkHistoryForm(ModelForm):
    class Meta:
        model = WorkHistory

class WorkHistoryUpdateForm(WorkHistoryForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital

class HospitalUpdateForm(HospitalForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class ProfessionalLiabilityInsuranceCoverageForm(ModelForm):
    class Meta:
        model = ProfessionalLiabilityInsuranceCoverage

class ProfessionalLiabilityInsuranceCoverageUpdateForm(ProfessionalLiabilityInsuranceCoverageForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class CallCoverageForm(ModelForm):
    class Meta:
        model = CallCoverage

class CallCoverageUpdateForm(CallCoverageForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class PracticeLocationInfoForm(ModelForm):
    class Meta:
        model = PracticeLocationInfo

class PracticeLocationInfoUpdateForm(PracticeLocationInfoForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class CertsForm(ModelForm):
    class Meta:
        model = Certs

class CertsUpdateForm(CertsForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class AddOfficeProceduresForm(ModelForm):
    class Meta:
        model = AddOfficeProcedures

class AddOfficeProceduresUpdateForm(AddOfficeProceduresForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class DisclosureQuestionsForm(ModelForm):
    class Meta:
        model = DisclosureQuestions

class DisclosureQuestionsUpdateForm(DisclosureQuestionsForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class DisclosureQuestionsExplainationsForm(ModelForm):
    class Meta:
        model = DisclosureQuestionsExplainations

class DisclosureQuestionsExplainationsUpdateForm(DisclosureQuestionsExplainationsForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

class MalpracticeClaimsForm(ModelForm):
    class Meta:
        model = MalpracticeClaims

class MalpracticeClaimsUpdateForm(MalpracticeClaimsForm):
    class Meta:
        all_fields_optional = True
    
    @classmethod
    def get_session(self):
        return self.DBSession

