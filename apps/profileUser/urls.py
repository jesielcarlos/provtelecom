from django.conf.urls import url
from django.urls import path, include
from apps.core.views import HomeView
from apps.profileUser.views import ProfileUpdateView


urlpatterns = [
    path('profile/<int:pk>', ProfileUpdateView.as_view(), name="profile"),
]
