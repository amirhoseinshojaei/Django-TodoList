from django import forms
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm,PasswordChangeForm


class CustomPasswordResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254,widget=forms.EmailInput(

        attrs={

            'autocomplete':'email',
            'class': 'form-control'
        }
    ))


class CustomSetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(label='New password',widget=forms.PasswordInput(

        attrs= {

            'autocomplete': 'current-password',
            'class': 'form-control'
        }
    ))

    new_password2 = forms.CharField(label='New password confirmation',widget=forms.PasswordInput(

        attrs= {

            'autocomplete': 'current-password',
            'class': 'form-control'
        }
    ))


class CustomPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(label='Old password',widget=forms.PasswordInput(

        attrs={

            'autocomplete': 'current-password',
            'class': 'form-control',
            'autofocus': True
        }
    ))


    new_password1 = forms.CharField(label='New password',widget=forms.PasswordInput(

        attrs={

            'autocomplete': 'new-password',
            'class': 'form-control'
        }
    ))


    new_password2 = forms.CharField(label='New password confirmation',widget=forms.PasswordInput(

        attrs={

            'autocomplete': 'new-password',
            'class': 'form-control'
        }
    ))



