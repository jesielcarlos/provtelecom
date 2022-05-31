from django.conf.urls import url
from django.urls import path, include
from apps.finance.views import ContasView


urlpatterns = [
    path('contas/', ContasView.as_view(), name="contas"),
]
