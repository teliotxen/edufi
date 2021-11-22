from django import forms
from app_account.models import Agreement
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
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