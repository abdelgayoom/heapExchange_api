

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
]
