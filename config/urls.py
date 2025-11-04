from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('apps.core.urls')),
    path('api/items/', include('apps.api.urls')),
    path('api/reports/', include('apps.reports.urls')),
]