from django.contrib import admin
from django.urls import path, include
import dj_rest_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('movies/', include('movies.api.urls'))
]
