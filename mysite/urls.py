from django.contrib import admin
from django.urls import path, include
from myweb import urls

urlpatterns = [
    path('', include('myweb.urls')),
    path('admin/', admin.site.urls),
   
]
