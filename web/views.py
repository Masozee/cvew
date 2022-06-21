from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse

from .models import *
# Create your views here.

def home(request):
   
    return render(request, "map.html",)

def home_id(request):
   
    return render(request, "index_id.html",)

