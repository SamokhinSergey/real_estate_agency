# Generated by Django 2.2.24 on 2022-05-28 09:26

from django.db import migrations
from django.db.models import Q


def change_newbuilding_fild(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    newbuilding_year = 2014
    Flat.objects.update(new_building=Q(construction_year__gte=newbuilding_year))


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(change_newbuilding_fild)
    ]
