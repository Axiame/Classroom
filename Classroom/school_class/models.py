from django.db import models
from schools.models import School
from users.models import Schoolie

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class ClassTeacher(models.Model):
    user = models.ForeignKey(Schoolie, on_delete=models.CASCADE)

class ClassUser(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='classroom')
    user = models.ForeignKey(Schoolie, on_delete=models.CASCADE, related_name='student')
