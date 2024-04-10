from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('loginInicio.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
