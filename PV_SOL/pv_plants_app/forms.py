from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import UpdateView

from .models import PV_Plant, UserProfile
from django import forms



class PVCreateForm(forms.ModelForm):
    class Meta:
        model = PV_Plant
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'power': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }
        fields = '__all__'

class PVUpdateForm(forms.ModelForm):
    class Meta:
        model = PV_Plant
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'power': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',  'email') #'password',
        widgets = {
                 'password': forms.PasswordInput

        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)    #fields = '__all__'


class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOISES = (
        (ORDER_ASC, 'Ascending'),
        (ORDER_DESC, 'Descending'),
                         )
    text = forms.CharField(required=False)
    order = forms.ChoiceField(
        choices=ORDER_CHOISES,
        required=False,
    )


class ForecastForm(forms.Form):
    number_of_days = forms.IntegerField(label='number_of_days')