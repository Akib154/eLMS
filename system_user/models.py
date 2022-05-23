from django.db import models

# Create your models here.

class Student(models.Model):
    stu_id = models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=300)
    description=models.TextField(max_length=500)

class Teacher(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=300)
    description=models.TextField(max_length=500)



