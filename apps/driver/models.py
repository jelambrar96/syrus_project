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

    def __str__(self): 
        return '%s %s' %(self.driver_name, self.driver_lastname)