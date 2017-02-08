from django import forms
from django.contrib.auth.models import User
from registration.models import UserProfile

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['website','picture']

# class LoginForm(forms.Form):
#     login = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def clean(self, *args, **kwargs):
#         login = self.cleaned_data.get('login')
#         password = self.cleaned_data.get('password')
#         user = authenticate(username=login, password=password)
#         if not user:
#             raise forms.ValidationError('Login failed')
#         return super(LoginForm, self).clean(*args, **kwargs)
#
# class RegisterForm(forms.Form):
#     login = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     passwordConfirm = forms.CharField(widget=forms.PasswordInput)
#
#     def clean(self, *args, **kwargs):
#         login = self.cleaned_data.get('login')
#         password = self.cleaned_data.get('password')
#         passwordConfirm = self.cleaned_data.get('passwordConfirm')
#
#         if (password!=passwordConfirm):
#             raise forms.ValidationError('Passwords do not match')
#
#         user = authenticate(username=login, password=password)
#
#         return super(RegisterForm, self).clean(*args, **kwargs)
