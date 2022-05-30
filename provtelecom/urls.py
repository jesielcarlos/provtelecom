from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import apps.profileUser.urls
import apps.callSystem.urls
import apps.services.urls

urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profileUser/', include('apps.profileUser.urls')),
    path('callSystem/', include('apps.callSystem.urls')),
    path('services/', include('apps.services.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
