# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_username = models.CharField(max_length = 12, blank = False)
    user_password = models.CharField(max_length = 48, blank = False)
    user_name = models.CharField(max_length = 24, blank = False)
    user_lastname = models.CharField(max_length = 24, blank = False)
    user_email = models.EmailField(blank = False)
    user_tel = models.CharField(max_length = 16, default = '')
    

    def __str__(self):
        return self.user_name
