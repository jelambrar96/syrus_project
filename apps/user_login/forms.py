from django import forms
from apps.user_login.models import User

class UserForm (forms.ModelForm):
    user_password = forms.CharField(widget = forms.PasswordInput)
    class Meta: 
        model = User