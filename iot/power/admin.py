from django.contrib import admin
from .models import PowerThings

@admin.register(PowerThings)
class PowerThingsAdmin(admin.ModelAdmin):
    pass 
