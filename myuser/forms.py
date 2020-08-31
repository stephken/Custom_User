from django import forms
from myuser.models import MyUser


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField()
    age = forms.IntegerField()
    homepage = forms.URLField()
    class Meta:
        model =MyUser
        fields = ['username', "password", "homepage", "display_name", "age"]


class LoginForm (forms.Form):
    username = forms.CharField(max_length= 200)
    password = forms.CharField(widget=forms.PasswordInput)