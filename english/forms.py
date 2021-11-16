from django import forms
from .models import uploadFileModel, Quiz


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = uploadFileModel
        fields = ['title', 'file']

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['file'].required = False

class DataTable(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['level','word1','word1_switch','word1_korean','word2',
                  'word2_switch','word2_korean','word3','word3_switch',
                  'word3_korean','english','korean']
