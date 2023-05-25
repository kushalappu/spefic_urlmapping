app_name='anything'
from django.urls import path
from app1.views import *
urlpatterns = [
    path('rcb/',rcb,name='rcb'),
]
