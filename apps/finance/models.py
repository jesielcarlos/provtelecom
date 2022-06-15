from django.db import models
from apps.profileUser.models import ProfileUser
from django.utils.translation import gettext as _


# class PaymentReceipt(models.Model):
#     active = models.BooleanField(verbose_name="Active", default=True)
#     dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
#     description = models.CharField(verbose_name="Description", max_length=300)
#     dt_payment = models.DateTimeField(verbose_name="Date Payment")


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

    OPEN = 0
    CLOSED = 1

    STATUS = (
        (OPEN, _('Open')),
        (CLOSED, _('Closed')),
    )

    active = models.BooleanField(verbose_name="Active", default=True)
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    profile = models.ForeignKey(ProfileUser, verbose_name="profile", on_delete=models.DO_NOTHING)
    # payment_receipt = models.ForeignKey(PaymentReceipt, verbose_name="Payment Receipt", on_delete=models.DO_NOTHING, null=True, blank=True)
    value = models.DecimalField(verbose_name="Value", max_digits=6, decimal_places=2)
    name = models.CharField(verbose_name="Name", max_length=150)
    dt_payment = models.DateTimeField(verbose_name="Date Payment", null=True, blank=True)
    dt_due = models.DateTimeField(verbose_name="Date Due")
    payment = models.IntegerField(verbose_name="Payment", choices=PAYMENTS, null=True, blank=True)
    status = models.IntegerField(verbose_name="Status", choices=STATUS, default=OPEN)

    def __str__(self):
        return self.name
        