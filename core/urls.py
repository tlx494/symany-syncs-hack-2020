from django.contrib import admin
from django.conf.urls import url
from django.urls import path

# internal imports 
from core import views

urlpatterns = [
    url(r'^document$', views.DocumentView.as_view(), name='document_view'),
    path('', admin.site.urls),
]
