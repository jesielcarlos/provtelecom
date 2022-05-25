from django.contrib import admin
from apps.finance.models import Contas, PaymentReceipt


admin.site.register(PaymentReceipt)
admin.site.register(Contas)
