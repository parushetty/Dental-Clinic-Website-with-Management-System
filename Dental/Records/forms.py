from django import forms
from .models import Treatment_Details



class TreatmentDetailsForm(forms.ModelForm):
    class Meta:
        model = Treatment_Details
        fields = ['visited_on','case_name','xray_taken','opg_taken','opg_images','case_status','payment_method','payment_status']


