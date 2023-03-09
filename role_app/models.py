from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _ 
# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField(_("Is Patient"), default= False)
    is_doctor = models.BooleanField(_("Is Doctor"), default= False)

class Paient(models.Model):
    paient = models.OneToOneField("User",related_name ="Patient_User",
                                   verbose_name=_("patient"), on_delete=models.CASCADE)
    ph_num = models.CharField(_("Phone Number"), max_length=15)
    survay = ''
    report = ''
    request = ''

class Doctor (models.Model):
    Doctor = models.OneToOneField("User", verbose_name=_("Doctor"),
                                   related_name="Doctor_User", on_delete=models.CASCADE)
    certificate = ''
    specialist = ''
