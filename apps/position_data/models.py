from django.db import models

# Create your models here.
class Position_data(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    datetime = models.DateTimeField()
    velocity = models.FloatField(default = 0)
    id_syrus = models.CharField(max_length = 16, default = '')

