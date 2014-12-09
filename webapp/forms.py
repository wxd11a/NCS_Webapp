from wtforms_alchemy import ModelForm
from wtforms_components import DateField
from .models import (
        IndividInfo,
        EducationBackground,
        PostGrad,
        IndividPostGrad,
        LicenseCertificates,
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

