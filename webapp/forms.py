from wtforms_alchemy import ModelForm#, ModelFieldList
from wtforms.fields import FormField
from wtforms_components import DateField
from .models import (
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
        IndividPracticeLoc,
        Certs,
        AddOfficeProcedures,
        DisclosureQuestions,
        DisclosureQuestionsExplainations,
        MalpracticeClaims
        )

# Douglas, using WTForm-Alchemy to generate the forms since Deform requires its own schema definition.
#   WTF-Alchemy ties its form schema to the SQLAlchemy model schema. This makes form generation manageable.

# Douglas, possibly could generate labels here to avaoid autoescaping the html
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

class PostGradForm(ModelForm):
    class Meta:
        model = PostGrad

class LicenseCertificateForm(ModelForm):
    class Meta:
        model = LicenseCertificate

class LicenseTypesForm(ModelForm):
    class Meta:
        model = LicenseTypes

class ProfessionalSpecialtyInfoForm(ModelForm):
    class Meta:
        model = ProfessionalSpecialtyInfo

class WorkHistoryForm(ModelForm):
    class Meta:
        model = WorkHistory

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital

class ProfessionalLiabilityInsuranceCoverageForm(ModelForm):
    class Meta:
        model = ProfessionalLiabilityInsuranceCoverage

class CallCoverageForm(ModelForm):
    class Meta:
        model = CallCoverage

class PracticeLocationInfoForm(ModelForm):
    class Meta:
        model = PracticeLocationInfo

class CertsForm(ModelForm):
    class Meta:
        model = Certs

class AddOfficeProceduresForm(ModelForm):
    class Meta:
        model = AddOfficeProcedures

class DisclosureQuestionsForm(ModelForm):
    class Meta:
        model = DisclosureQuestions

class DisclosureQuestionsExplainationsForm(ModelForm):
    class Meta:
        model = DisclosureQuestionsExplainations

class MalpracticeClaimsForm(ModelForm):
    class Meta:
        model = MalpracticeClaims

