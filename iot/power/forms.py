from django.forms import ModelForm
from power.models import PowerThings
from django.utils.translation import ugettext_lazy as _

class PowerThingsForm(ModelForm):
    class Meta:
        model = PowerThings
        fields = ['light1', 'light2', 'toaster', 'nuclearDefenseSystem']
        labels = {
            'light1': _('Front Door Light'),
            'light2': _('Floodlight'),
            'toaster': _('Toaster Oven'),
            'nuclearDefenseSystem': _('Nuclear Defense System')
        }
