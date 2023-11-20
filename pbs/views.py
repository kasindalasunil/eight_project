from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dawan(request):
    return render(request,'dawan.html')

def liam(request):
    return HttpResponse('<h1>he is the best hitter for pbs</h1>')

