# Generated by Django 3.1.3 on 2020-11-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pv_plants_app', '0002_auto_20201124_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='pv_plant',
            name='power',
            field=models.TextField(default=10),
            preserve_default=False,
        ),
    ]