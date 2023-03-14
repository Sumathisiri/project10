from app2.views import *
from django.urls import path
app_name='hello'



urlpatterns=[
    path('project10/',project10,name='project10'),
    path('project/',project,name='project'),
]