# Generated by Django 3.1.3 on 2020-12-04 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pv_plants_app', '0007_pv_plant_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pv_plant',
            name='created_by',
        ),
    ]