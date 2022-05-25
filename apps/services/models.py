from django.db import models
from django.db import models
from django.utils.translation import gettext as _


class ServicePlan(models.Model):
    INTENET = 0
    VOIP = 1

    TYPES = (
        (INTENET, _('Internet')),
        (VOIP, _('Voip')),

    )
    active = models.BooleanField(verbose_name="Active", default=True)
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=150)
    value = models.DecimalField(verbose_name="Plan Value", max_digits=6, decimal_places=2)
    description = models.CharField(verbose_name="Description", max_length=300)
    type_service = models.IntegerField(verbose_name="Type Service", choices=TYPES)
    velocity = models.IntegerField(verbose_name="Velocity", null=True, blank=True)
    bandwidth = models.IntegerField(verbose_name="Bandwidth", null=True, blank=True)


    def __str__(self):
        return self.name
