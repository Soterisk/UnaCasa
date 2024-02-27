from django.forms import forms

from ResaleApp.models import ResaleThings, ResaleImage


class ResaleThingsForm(forms.ModelForm):
    class Meta:
        model = ResaleThings
        fields = ['title', 'description', 'price']

class ResaleImageForm(forms.ModelForm):
    class Meta:
        model = ResaleImage
        fields = ['image']