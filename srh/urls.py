from srh.views import *

from django.urls import path

app_name='jingilala'

urlpatterns=[
    path('mark/',mark,name='mark'),
    path('klassan/',klassan,name='klassan'),
]