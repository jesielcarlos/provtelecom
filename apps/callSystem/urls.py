from django.conf.urls import url
from django.urls import path, include
from apps.callSystem.views import CalledCreateView, CalledView


urlpatterns = [
    path('called/', CalledView.as_view(), name="called"),
    path('creat-called/', CalledCreateView.as_view(), name="creat_called"),
]
