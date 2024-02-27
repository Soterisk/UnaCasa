from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


username_validator = ASCIIUsernameValidator()


class CustomUser(AbstractUser):
    username = models.CharField(('username'), max_length=30, unique=True, help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'), validators=[username_validator], error_messages={'unique': _("A user with that username already exists.")})
    email = models.EmailField(('email address'), unique=True)
    tel_num = models.CharField(max_length=20, blank=True, null=True)
    is_agent = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'tel_num']

class Agent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'agent'


