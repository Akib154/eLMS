from django.urls import path
from .views import *

urlpatterns =[
    
    path('',getUser),
    path('t/',getTeacher),
]