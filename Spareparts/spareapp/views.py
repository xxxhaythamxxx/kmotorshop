from django.shortcuts import render
from .models import *
from django.views import View
# Create your views here.
def home(request):
    return render(request,"spareapp/home.html")

def find(request):
    return render(request,"spareapp/find.html")