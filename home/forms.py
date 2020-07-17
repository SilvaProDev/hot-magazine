from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.forms import UserCreationForm

from .models import ContactMessage


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='username')
    email = forms.EmailField(max_length=100, label='email adres')
    first_name = forms.CharField(max_length=100, help_text='', label='FirtName')
    last_name = forms.CharField(max_length=100, help_text='', label='LastName')

    class Meta():
        model=User
        fields = ('username', 'email', 'first_name', 'last_name','password1', 'password2',)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=50)

class ContactForm(forms.ModelForm):

    class Meta():
        model = ContactMessage
        fields = ('name', 'email', 'message')





                    


        

