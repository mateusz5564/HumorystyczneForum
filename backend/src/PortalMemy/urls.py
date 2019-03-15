
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
