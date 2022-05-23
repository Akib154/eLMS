from django.shortcuts import render
from .models import *

# Create your views here.

def getUser(request):
    stu=Student.objects.all()
    return render(request,'system_user/user.html',{'akib':stu})

def getTeacher(request):
    teacher=Teacher.objects.all()
    return render(request,'system_user/user1.html',{'list':teacher})