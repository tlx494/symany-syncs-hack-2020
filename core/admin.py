from django.contrib import admin

import django.contrib.auth.admin
from django.contrib.auth.models import User, Group
from django.contrib import auth

from .models import Document

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Document)
