# Generated by Django 4.1.3 on 2022-12-21 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cwiczenia', '0009_remove_rekordy_create_date_rekordy_nazwa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rekordy',
            old_name='rekord',
            new_name='rekord_kg',
        ),
    ]