from app1.views import *
from django.urls import path
app_name='Be happy'

urlpatterns=[
    path('jinja_print/',jinja_print,name='jinja_print'),
    path('second/',second,name='second'),

]