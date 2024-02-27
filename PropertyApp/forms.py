from django.forms import forms

from PropertyApp.models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['street', 'zip_code', 'city', 'country', 'num_of_bedrooms', 'num_of_bathrooms', 'bills_included', 'description']
