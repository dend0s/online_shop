from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .validators import phone_number_validator


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(' Пользователь с таким Email уже существует')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Пользователь с таким номером телефона уже существует')
        return phone_number_validator(phone_number)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name.capitalize()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(' Пользователь с таким Email уже существует')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Пользователь с таким номером телефона уже существует')
        return phone_number_validator(phone_number)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name.capitalize()
