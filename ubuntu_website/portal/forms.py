from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ServiceRequest, Opportunity, Application

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['title', 'category', 'description', 'urgency']

class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ['title', 'type', 'description', 'deadline']
        widgets = {'deadline': forms.DateInput(attrs={'type': 'date'})}

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['message']