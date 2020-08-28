from django.contrib import admin
from django.conf.urls import url
from django.urls import path

# internal imports 
from core import views

urlpatterns = [
    path('', admin.site.urls),
]
