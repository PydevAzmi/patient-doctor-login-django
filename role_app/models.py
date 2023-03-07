from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _ 
# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField(_("Is Patient"), default= False)
    is_doctor = models.BooleanField(_("Is Doctor"), default= False)