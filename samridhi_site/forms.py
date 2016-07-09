from django import forms
from .models import Baseline
from .models import Enrollments
from .models import Health
from .models import Academics


class BaselineForm(forms.ModelForm):
     class Meta:
         model=Baseline
         fields=('id','name','fname','native_lang','siblings','photo','age','date')


class EnrollmentForm(forms.ModelForm):
       class Meta:
       model=Enrollments
       fields=('id','name','fname','native_lang','survey_taken','siblings','photo','age','date')

class AcademicsForms(forms.ModelForms):
       class Meta:
            model=Academics
            fields=('id','name','date','math','science','english','hindi','extracuricular_activities')
            
            
class HealthForms(forms.ModelForms):
       class Meta:
           model=Health
           fields=('id','name','date','student_health','fathers_health','mothers_health','siblings_health')
