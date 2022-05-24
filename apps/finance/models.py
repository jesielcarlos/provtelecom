from django.db import models
from apps.profileUser.models import ProfileUser
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
    profile = models.ForeignKey(ProfileUser, verbose_name="profile", on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name="Name", max_length=150)
    type_service = models.IntegerField(verbose_name="Type Service", choices=TYPES)

    def __str__(self):
        return self.name


class PaymentReceipt(models.Model):
    active = models.BooleanField(verbose_name="Active", default=True)
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    profile = models.ForeignKey(ProfileUser, verbose_name="profile", on_delete=models.DO_NOTHING)
    description = models.CharField(verbose_name="Description", max_length=300)
    dt_payment = models.DateTimeField(verbose_name="Date Payment")


class Contas(models.Model):

    CARD = 0
    BANK_TICKET = 1
    PIX = 2
    BANK_TRANSFER = 3

    PAYMENTS = (
        (CARD, _('Card')),
        (BANK_TICKET, _('Bank Ticket')),
        (PIX, _('Pix')),
        (BANK_TRANSFER, _('Bank Transfer')),
    )
    active = models.BooleanField(verbose_name="Active", default=True)
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    profile = models.ForeignKey(ProfileUser, verbose_name="profile", on_delete=models.DO_NOTHING)
    service_plan = models.ForeignKey(ServicePlan, verbose_name="Service Plan", on_delete=models.DO_NOTHING)
    payment_receipt = models.ForeignKey(PaymentReceipt, verbose_name="Payment Receipt", on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name="Name", max_length=150)
    dt_payment = models.DateTimeField(verbose_name="Date Payment", null=True, blank=True)
    dt_due = models.DateTimeField(verbose_name="Date Due")
    payment = models.IntegerField(verbose_name="Payment", choices=PAYMENTS)
    