from django.contrib import admin
from apps.finance.models import Contas, PaymentReceipt, ServicePlan


admin.site.register(ServicePlan)
admin.site.register(PaymentReceipt)
admin.site.register(Contas)
