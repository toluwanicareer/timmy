from django import forms
from django.contrib.auth.models import User
from acc.models import Profile



class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')

        widgets={
        'first_name':forms.TextInput(attrs={'class':'form-control borderprob'}),
        'last_name':forms.TextInput(attrs={'class':'form-control borderprob'}),
        'username':forms.TextInput(attrs={'class':'form-control borderprob'}),
        'email':forms.EmailInput(attrs={'class':'form-control borderprob'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('picture','phone', 'bit_address')

        widgets={
        'bit_address':forms.TextInput(attrs={'class':'form-control'}),
        }

