# Generated by Django 2.0.3 on 2018-03-07 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('position_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position_data',
            old_name='datatime',
            new_name='datetime',
        ),
    ]
