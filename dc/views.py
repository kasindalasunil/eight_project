from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def pant(request):
    return render(request,'pant.html')

def iyer(request):
    return HttpResponse('<h1>he is the most consistent player</h1>')

