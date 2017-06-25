from django import forms
from power.models import PowerThings
from django.utils.translation import ugettext_lazy as _

class PowerThingsForm(forms.ModelForm):
    class Meta:
        model = PowerThings
        fields = '__all__'

    widgets={
        'light1': forms.CheckboxInput(attrs={'id':'light1', 'checked': ''}),
	'light2': forms.CheckboxInput(attrs={'id':'light2', 'checked': ''}),
	'light3': forms.CheckboxInput(attrs={'id':'light3', 'checked': ''}),
        'light4': forms.CheckboxInput(attrs={'id':'light4', 'checked': ''}),
    }
