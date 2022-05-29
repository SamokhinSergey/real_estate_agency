# Generated by Django 2.2.24 on 2022-05-28 12:11
import phonenumbers

from django.db import migrations


def normalize_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        normalized_phone_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(normalized_phone_number):
            flat.owner_pure_phone = f'+{normalized_phone_number.country_code}{normalized_phone_number.national_number}'
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20220528_1551'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_number)
    ]
