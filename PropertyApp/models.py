from django.db import models

class Property(models.Model):
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    num_of_bedrooms = models.IntegerField()
    num_of_bathrooms = models.IntegerField()
    bills_included = models.BooleanField(default=False)
    property_num = models.AutoField(primary_key=True)
    agent = models.ForeignKey('UserApp.Agent', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    date_listed = models.DateTimeField(auto_now_add=True)
    date_unavailable = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.street}, {self.city}, {self.country}'