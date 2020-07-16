from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placholder':'Username'}), required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placholder':'first_name'}), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placholder':'last_name'}), required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placholder':'Email'}), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}), required=True, max_length=20)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}), required=True, max_length=20)

    class Meta():
        model= User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean_username(self):
        user = self.cleaned_data['username']
        try:
            match = User.objects.get(username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidatonError("Ce nom existe deja ")
        
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            my = validate_email(email)
        except:
            return forms.ValidatonError("email incorrect")
        return email

    def clean_confirm_password(self):
        pas = self.cleaned_data['password']
        cpas = self.cleaned_data['confirm_data']
        MIN_LENGTH = 8
        if pas and cpas:
            if pas != cpas:
                raise forms.ValidationError("Mot de passe different")
            else:
                if len(pas) < MIN_LENGTH:
                    raise forms.ValidationError("paassword should atlest %s characters"%MIN_LENGTH)
                if pas.isdigit():
                    raise forms.ValidationError("Password should not all numeric")


class SearchForm(forms.Form):
    query = forms.CharField(max_length=50)

                    


        

