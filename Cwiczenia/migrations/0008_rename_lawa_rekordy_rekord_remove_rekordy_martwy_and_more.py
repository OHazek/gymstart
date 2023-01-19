# Generated by Django 4.1.3 on 2022-12-20 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cwiczenia', '0007_rekordy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rekordy',
            old_name='lawa',
            new_name='rekord',
        ),
        migrations.RemoveField(
            model_name='rekordy',
            name='martwy',
        ),
        migrations.RemoveField(
            model_name='rekordy',
            name='przysiad',
        ),
        migrations.AddField(
            model_name='rekordy',
            name='cwiczenie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Cwiczenia.cwiczenia'),
        ),
    ]