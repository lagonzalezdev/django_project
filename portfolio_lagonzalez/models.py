from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import URLField
# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    lenguage = CharField(max_length= 100)
    url_github = URLField(blank=True)
    url_deploy = URLField(blank=True)