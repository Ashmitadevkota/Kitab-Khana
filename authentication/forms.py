from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.utils.translation import  gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm, UsernameField

from django.core import validators
def validete_username(value):
    if len(value)<=2:
        raise forms.ValidationError(f"Your username cannot be of {len(value)}  word")

class UserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={"placeholder":"Password",'autocomplete':'new-password'}),error_messages={"required":"Please enter password"},)
    password2 = forms.CharField(label="Re-enter",widget= forms.PasswordInput(attrs={"placeholder":"Re-enter Password",'autocomplete':'new-password'}),help_text="Make sure your password contains 'small letter','capital letter','numbers' and 'symbols'",error_messages={"required":"Re-Enter password field cannot be empty"})
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={"placeholder":"Username","id":"username"}),validators=[validete_username],error_messages={'required':'Username is required'})
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name","required":True}),error_messages={"required":"First name cannot be empty"})
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name","required":True}),error_messages={"required":"Last name cannot be empty"})
    email = forms.CharField(widget=forms.EmailInput(attrs={"required":True,"Placeholder":"Email",'autocomplete':'username'}),error_messages={'required':'Email field cannot be felt empty'})
    class  Meta:
        model = User
        fields =['username','email','first_name','last_name','password1','password2']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"placeholder":"Username"}),error_messages={'required':'Username is required'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password",'autocomplete':'current-password'}),error_messages={'required':'Password is required'})    
        
        
       
       
        
        
        
