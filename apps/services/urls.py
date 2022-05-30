from django.conf.urls import url
from django.urls import path, include
from apps.services.views import ServicePlanView


urlpatterns = [
    path('service-plans/', ServicePlanView.as_view(), name="service_plans"),
]
