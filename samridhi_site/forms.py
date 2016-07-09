from django import forms
from .models import Baseline
from .models import Enrollment
from .models import Health
from .models import Academics


class BaselineForm(forms.ModelForm):
     class Meta:
         model=Baseline
         fields=('id','name','fname','native_lang','siblings','photo','age','date')


class EnrollmentForm(forms.ModelForm):
    class Meta:
       model=Enrollment
       fields=('id','name','fname','native_lang','survey_taken','siblings','photo','age','date')

class AcademicsForms(forms.ModelForm):
       class Meta:
            model=Academics
            fields=('id','name','date','maths','science','english','hindi','extracuricular_activities')


class HealthForms(forms.ModelForm):
       class Meta:
           model=Health
           fields=('name','student_health','fathers_health','mothers_health')
