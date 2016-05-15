from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from forms import *
import RPi.GPIO as GPIO

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

    if request.method == "GET":
        last = PowerThings.objects.count()
        if last > 0:
            pt_last = PowerThings.objects.get(pk=last)
            pt = PowerThingsForm(initial={"light1":checks, "light2":checks, "toaster":checks, "nuclearDefenseSystem":checks})
            
        
 
    if request.method == "POST":
        form = PowerThingsForm(request.POST)

        if form.is_valid():
            light1 = form.cleaned_data["light1"]
            light2 = form.cleaned_data["light2"]
            toaster = form.cleaned_data["toaster"]
            nuclearDefenseSystem = form.cleaned_data["nuclearDefenseSystem"]
            
            pt = PowerThings()
            pt.light1 = light1
            pt.light2 = light2
            pt.toaster = toaster
            pt.nuclearDefenseSystem = nuclearDefenseSystem
            pt.save()
            
            turn_on_off("light1", light1) 
            turn_on_off("light2", light2)
            turn_on_off("toaster", toaster)
            turn_on_off("nuclearDefenseSystem", nuclearDefenseSystem)

    context = {
        'request': request,
        'form': form,
    }

    return HttpResponse(template.render(context, request))

def turn_on_off(device, on_mode):
    device_pin = None   
    if on_mode:
        on_off = GPIO.HIGH
    else:
        on_off = GPIO.LOW

    if device == "light1":
    	device_pin = 17
    elif device == "light2":
        device_pin = 27
    elif device == "toaster":
        device_pin = 22
    elif device == "nuclearDefenseSystem":
        device_pin = 23
    else:
        return 
    
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup(device_pin)
    GPIO.setwarnings(False)
    GPIO.setup(device_pin, GPIO.OUT)

    GPIO.output(device_pin, on_off)
    print "Device:", device, ", Status:", on_mode

