from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from forms import *

def index(request):
    template = loader.get_template('power/index.html')
    return HttpResponse(template.render(request))

def power_main(request):
    template = loader.get_template('power/power_main.html')
    form = PowerThingsForm()
    
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def enabler(request):
    template = loader.get_template('power/power_main.html')
    form = PowerThingsForm()

    context = {
        'request': request,
        'form': form,
    }

    if form.is_valid():
        light1 = form.cleaned_data["light1"]
        light2 = form.cleaned_data["light2"]
        toaster = form.cleaned_data["toaster"]
        nuclearDefenseSystem = form.cleaned_data["nuclearDefenseSystem"]
        
        print light1
        print light2
        print toaster
        print nuclearDefenseSystem
    
    return HttpResponse(tempalte.render(context, request))
