from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

GENDER_CHOICES = [
    ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')
]


class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'type': 'text'}))
    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email',
                  'date_of_birth', 'phone', 'gender']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['date_of_birth']
