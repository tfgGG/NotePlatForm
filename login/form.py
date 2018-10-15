from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Profile

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password']

    def clean(self):
        return self.cleaned_data

'''
username = self.cleaned_data.get('username')
           password = self.cleaned_data.get('password')
           user = authenticate(username=username, password=password)
           if not user or not user.is_active:
               raise forms.ValidationError("Sorry, that login was invalid. Please try again.")

'''

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['school','grade','birth','intro']

    def clean(self):
            return self.cleaned_data
'''
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        email = self.cleaned_data['school']
        birth = self.cleaned_data['birth']
        intro = self.cleaned_data['intro']
        grade = self.cleaned_data['grade']

        if commit:
            user.save()

        return user
'''
class AuthForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password','email']
        help_texts = {
            'username': None,
        }

    def clean(self):
        return self.cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get('password')
        #nextpassword = self.cleaned_data.get("nextpassword")
        #if password != nextpassword:
        #    errors['pass1'] = ValidationError('Password no match', code='code1')
        if len(password)<5:
            raise forms.ValidationError('Password  must contain more than five character')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email exists already. Please use a different email address.")
        if validate_email(email):
            #errors_list.append( ValidationError("Not a valiable email")
            raise forms.ValidationErrors("Not a valiable email")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError("Usernamehas been used. Please use a different username")
        return username
