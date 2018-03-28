# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length = 24, default = '')
    user_lastname = models.CharField(max_length = 24, default = '')
    user_email = models.EmailField()
    drive_tel = models.CharField(max_length = 16, default = '')

    def __str__(self):
        return self.user_name
        