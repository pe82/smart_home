from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from power.forms import *
import RPi.GPIO as GPIO

def index(request):
    return render(request, 'power/index.html')

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
            pt = PowerThingsForm(initial={"light1":checks, "light2":checks, "light3":checks, "light4":checks})
            
        
 
    if request.method == "POST":
        form = PowerThingsForm(request.POST)

        if form.is_valid():
            light1 = form.cleaned_data["light1"]
            light2 = form.cleaned_data["light2"]
            light3 = form.cleaned_data["light3"]
            light4 = form.cleaned_data["light4"]
            
            pt = PowerThings()
            pt.light1 = light1
            pt.light2 = light2
            pt.light3 = light3
            pt.light4 = light4
            pt.save()
            
            turn_on_off("light1", light1) 
            turn_on_off("light2", light2)
            turn_on_off("light3", light3)
            turn_on_off("light4", light4)

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
        device_pin = 23
    elif device == "light3":
        device_pin = 27
    elif device == "light4":
        device_pin = 22
    else:
        return 
    
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup(device_pin)
    GPIO.setwarnings(False)
    GPIO.setup(device_pin, GPIO.OUT)

    GPIO.output(device_pin, on_off)
    print ("Device:", device, ", Status:", on_mode)

