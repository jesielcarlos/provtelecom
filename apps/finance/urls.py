from django.conf.urls import url
from django.urls import path, include
from apps.finance.views import ContaPrintView, ContasView, PaymentReceiptPrintView


urlpatterns = [
    path('contas/', ContasView.as_view(), name="contas"),
    path('payment-receipt-print/<int:pk>', PaymentReceiptPrintView.as_view(), name="payment_receipt_print"),
    path('conta-print/<int:pk>', ContaPrintView.as_view(), name="conta_print"),
]
