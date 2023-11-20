from pbs.views import *

from django.urls import path

app_name='fasak'

urlpatterns=[

    path('dawan/',dawan,name='dawan'),
    path('liam/',liam,name='liam'),
    

]