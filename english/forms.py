from django import forms
from .models import uploadFileModel


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = uploadFileModel
        fields = ['title', 'file']

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['file'].required = False