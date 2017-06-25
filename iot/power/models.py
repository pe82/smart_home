from __future__ import unicode_literals

from django.db import models

class PowerThings(models.Model):
    light1 = models.BooleanField()
    light2 = models.BooleanField()
    light3 = models.BooleanField()
    light4 = models.BooleanField()
