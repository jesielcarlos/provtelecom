from django.conf.urls import url
from django.urls import path, include
from apps.core.views import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
]
