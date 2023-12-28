from django.db import models
from users.models import Schoolie

class School(models.Model):
    name = models.CharField(max_length=100)
    localisation = models.CharField(max_length=100)

class SchoolAdmin(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schools')
    user = models.ForeignKey(Schoolie, on_delete=models.CASCADE, related_name='schools_admin')
