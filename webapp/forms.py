from wtforms_alchemy import ModelForm
from wtforms_components import DateField
from .models import Individ_Info, Education_Background

# Douglas, using WTForm-Alchemy to generate the forms since Deform requires its own schema definition.
#   WTF-Alchemy ties its form schema to the SQLAlchemy model schema. This makes form generation manageable.
class Individ_Info_Form(ModelForm):
    class Meta:
        model = Individ_Info

class Education_Background_Form(ModelForm):
    class Meta:
        model = Education_Background

