from django.conf.urls import url
from django.urls import path, include
from apps.core.views import ContractView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contract', ContractView.as_view(), name="contract"),
]
