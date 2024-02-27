from django import forms

from ReferralApp.models import Referral, ReferralImage



class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['agent_email', 'personal_exp', 'availability_date', 'current_rent']

class ReferralImageForm(forms.ModelForm):
    class Meta:
        model = ReferralImage
        fields = ['image']
