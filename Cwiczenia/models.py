from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth




class Partie(models.Model):
    def __str__(self):
        return self.nazwa +" "
    nazwa = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Partia"
        verbose_name_plural = "Partie"


class Cwiczenia(models.Model):
    def __str__(self):
        return self.nazwa+" "
    partia = models.ForeignKey(Partie, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    film = models.TextField(blank=True)

    class Meta:
        verbose_name = "Cwiczenie"
        verbose_name_plural = "Cwiczenia"



class Rekordy(models.Model):
    class Meta:
        verbose_name = "Rekord"
        verbose_name_plural = "Rekordy"

    nazwa = models.CharField(max_length=100, default='rekord')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Uzytkownik')
    cwiczenie = models.ForeignKey(Cwiczenia, on_delete=models.CASCADE, null=True)
    rekord_kg = models.FloatField()


class Plany(models.Model):
    def __str__(self):
        return self.nazwa+" "
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)


    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plany"







