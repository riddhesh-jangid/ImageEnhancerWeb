from pyexpat import model
from django.db import models

class UploadResolutionImage(models.Model):
    image = models.ImageField(upload_to='images')

class UploadLightImage(models.Model):
    image = models.ImageField(upload_to='images')


