from django import forms
from .models import Baseline
from .models import Enrollment

class BaselineForm(forms.ModelForm):
     class Meta:
         model=Baseline
         fields=('id','name','fname','native_lang','siblings','photo','age','date')


class EnrollmentForm(forms.ModelForm):
    class Meta:
       model=Enrollment
       fields=('id','name','fname','native_lang','survey_taken','siblings','photo','age','date')
