from django import forms
from django.core.files.storage import default_storage


class UploadImgForm(forms.Form):
    img = forms.ImageField(required=True, label='')
