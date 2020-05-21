

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/', include('allauth.urls')),
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/register/', include('rest_auth.registration.urls')),
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
]
