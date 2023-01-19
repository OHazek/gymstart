# Generated by Django 4.1.3 on 2022-12-24 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cwiczenia', '0010_rename_rekord_rekordy_rekord_kg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plany',
            },
        ),
    ]
