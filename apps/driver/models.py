# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models 

# Create your models here.
class Driver(models.Model):
    driver_name = models.CharField(max_length = 24, blank = False)
    driver_password = models.CharField(max_length = 48, blank = False)
    driver_lastname = models.CharField(max_length = 24, blank = False)
    id_syrus = models.CharField(max_length = 16, blank = False)
    driver_email = models.EmailField()
    driver_ciu = models.IntegerField()
    drive_tel = models.CharField(max_length = 16, blank = False)
    

    def __str__(self): 
        return '%s %s' %(self.driver_name, self.driver_lastname)