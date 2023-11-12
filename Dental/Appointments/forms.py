from django import forms
from .models import Appointment_Request
from django.contrib.auth.forms import AuthenticationForm

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment_Request
        fields = ['name','phone_number','email','service_required','location']

    
        name= forms.CharField(
            error_messages = {'required': 'Please enter your name!'}
        )

        phone_number = forms.CharField(
            error_messages = {'required': 'Please enter mobile number!'}
        )

        location = forms.CharField(
            error_messages = {'required': 'Please enter your location!'}
        )



class CustomLoginForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and not custom_username_validation(username):
            raise forms.ValidationError('Username validation failed.')

        if password and not custom_password_validation(password):
            raise forms.ValidationError('Password validation failed.')

def custom_username_validation(username):
    if len(username) < 5:
        return False
    if not username.isalnum():
        return False
    return True

def custom_password_validation(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_+=[]" for char in password):
        return False
    return True



