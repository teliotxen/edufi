from django import forms
from django.core.exceptions import ValidationError


from django.contrib.auth.models import User, AbstractUser

import app_account.models
from app_account.models import Agreement, Router
# from app_account.models import AbstractUser


class UserForm(forms.ModelForm):
    class Meta:
        model = app_account.models.User
        fields = ['username', 'password']


class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ['term_agreement', 'private_agreement', 'geoLocation_agreement', 'provide_third_parties_agreement', 'marketing_agreement', 'email_marketing_agreement', 'sms_agreement', ]
        widgets = {
            'term_agreement': forms.CheckboxInput,
            'private_agreement': forms.CheckboxInput,
            'geoLocation_agreement': forms.CheckboxInput,
            'provide_third_parties_agreement': forms.CheckboxInput,
            'marketing_agreement': forms.CheckboxInput,
            'email_marketing_agreement': forms.CheckboxInput,
            'sms_agreement': forms.CheckboxInput,
        }


from .models import User
class AditionalInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['name','email','birthday','school','gender']
        widgets = {
            # 'birthday' : ,
        }

class RouterForm(forms.ModelForm):
    class Meta:
        model = Router
        fields = ['get_time', 'max_time', 'free_time']