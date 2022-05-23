from django.db import models

# Create your models here.

class course(models.Model):
    name = models.CharField(max_length=128)
    course_code = models.CharField(max_length=50)
    section = models.CharField(max_length=10)

    