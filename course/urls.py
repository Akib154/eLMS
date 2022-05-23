from django.urls import path
from .views import getAllCourse

urlpatterns =[
    path('',getAllCourse)
]