from django.db import models

class Referral(models.Model):
    referral_num = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserApp.CustomUser', on_delete=models.CASCADE)  # New field
    property = models.ForeignKey('PropertyApp.Property', on_delete=models.CASCADE)
    agent_email = models.ForeignKey('UserApp.Agent', on_delete=models.CASCADE)
    personal_exp = models.TextField(null=True, blank=True)
    availability_date = models.DateField(null=True, blank=True)
    current_rent = models.DecimalField(max_digits=8, decimal_places=2)
    resale_things = models.ForeignKey('ResaleApp.ResaleThings', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Referral for {self.property}'

class ReferralImage(models.Model):
    image = models.ImageField(upload_to='referral_images/')
    referral = models.ForeignKey('ReferralApp.Referral', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'Image for Referral: {self.referral.id}'