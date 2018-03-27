# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Driver(models.Model):
    driver_name = models.CharField(max_length = 24, default = '')
    driver_lastname = models.CharField(max_length = 24, default = '')
    id_syrus = models.CharField(max_length = 16, default = '')
    driver_email = models.EmailField()
    driver_ciu = models.IntegerField()
    drive_tel = models.CharField(max_length = 16, default = '')

"""
class Position_data(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    datetime = models.DateTimeField()
    velocity = models.FloatField(default = 0)
    id_syrus = models.CharField(max_length = 16, default = '')
"""