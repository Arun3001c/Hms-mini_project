from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class DoctorApplicationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'qualification', 'location', 'experience', 'email', 'phone', 'languages']

class PatientAppointmentForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'dob', 'gender', 'mobile', 'address', 'email', 'disease', 'appointmentdate']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'appointmentdate': forms.DateInput(attrs={'type': 'date'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'patient_gender', 'patient_address', 'patient_email', 'patient_disease', 'patient_mobile']

class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminCred
        fields = ['admin_username', 'admin_password']
        