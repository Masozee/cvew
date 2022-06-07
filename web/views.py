from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse

from .models import *
# Create your views here.

def home(request):
   
    return render(request, "map.html",)

class index(TemplateView):
    template_name= 'map.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["qs"] = province.objects.all()
        return context

