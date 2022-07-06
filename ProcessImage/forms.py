from django.db import models
from django.forms import fields
from .models import UploadLightImage, UploadResolutionImage
from django import forms


class ResolutionImageForm(forms.ModelForm):
    class Meta:
        model = UploadResolutionImage
        fields = '__all__'


class LightImageForm(forms.ModelForm):
    class Meta:
        model = UploadLightImage
        fields = '__all__'