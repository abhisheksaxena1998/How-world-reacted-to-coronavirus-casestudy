#!/usr/bin/python
# -*- coding: utf-8 -*-
def warn(*args, **kwargs):
    pass

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import *


# Create your views here.

'''def error_404_view(request, exception):
    return render(request,'404.html')'''

def index(request):
    return render(request, 'index.html')
    


def about(request):
    #return HttpResponse("about")
    return render(request, 'about.html')

    
def experience(request):
    return render(request,'experience.html')

def my_skills(request):
    return render(request,'my_skills.html')



def getdataset(request):
    return render(request,'getdataset.html')
    
			
