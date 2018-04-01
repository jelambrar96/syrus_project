# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from apps.driver.models import Driver

# Register your models here.
class DriverAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Driver, DriverAdmin)