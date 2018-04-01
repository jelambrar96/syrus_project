from django.contrib import admin

from apps.position_data.models import Position_data

# Register your models here.

class Position_dataAdmin(admin.ModelAdmin):
    pass

admin.site.register(Position_data, Position_dataAdmin)
