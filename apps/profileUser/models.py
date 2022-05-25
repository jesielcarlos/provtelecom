import email
from django.conf import settings
from django.db import models
from apps.services.models import ServicePlan



class ProfileUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.DO_NOTHING)
    active = models.BooleanField(verbose_name="Active", default=True)
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    theme_dark = models.BooleanField(verbose_name="Theme Dark", default=True, null=True, blank=True)
    service_plan = models.ForeignKey(ServicePlan, verbose_name="Service Plan", on_delete=models.DO_NOTHING)
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    city = models.CharField(max_length=200, verbose_name="Cidade")
    address = models.CharField(max_length=200, verbose_name="Rua")
    cep = models.CharField(max_length=200, verbose_name="CEP")
    number = models.CharField(max_length=10, verbose_name="Número")
    district = models.CharField(max_length=200, verbose_name="Bairro")


    def __str__(self):
        return self.user.username
