import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import Cwiczenia, Partie, Rekordy, Plany
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import RekordForm
from datetime import date

def index(request):
    #kategoria = Cwiczenia.objects.filter(partia=2)
    context = {}
    if request.user.is_authenticated:
        # Do something for authenticated users.
        context['userStatus'] = 'zalogowany'
    else:
        # Do something for anonymous users.
        context['userStatus'] = 'niezalogowany'

    partie = Partie.objects.all()
    dane = {'partie' : partie, 'context': context}
    return render(request, 'home.html', dane)


def rejestracja(request):
    context = {}
    if request.method == 'POST':

        try:
            # sprawdzenie czy uzytkonik o takiej nazwie juz istnieje
            user = User.objects.get(username=request.POST['username'])
            context['error'] = 'Podana nazwa użytkownika już istnieje! Proszę podać inną nazwę użytkownika.'
            return render(request, 'rejestracja.html', context)
        except User.DoesNotExist:
            # Sprawdzenie hasel
            if request.POST['password1'] != request.POST['password2']:
                context['error'] = 'Podane hasła nie są takie same! Proszę wprowadzić identyczne hasła.'
                return render(request, 'rejestracja.html', context)
            else:
                # tworzenie uzytkoniwnika
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # automatyczne logowanie po rejestracji
                auth.login(request, user)
                # powrot na strone glowna
                return redirect('index')
    else:
        return render(request, 'rejestracja.html', context)


def logowanie(request):
    context = {}
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            context['error'] = 'Podane hasło lub login są błędne! Podaj poprawne dane.'
            return render(request, 'logowanie.html', context)
    else:
        return render(request, 'logowanie.html')


def wylogowanie(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')



def partia (request, id):
    partia_user = Partie.objects.get(pk=id)
    partia_cwiczenie = Cwiczenia.objects.filter(partia = partia_user)
    partie = Partie.objects.all()
    dane = {'partia_user' : partia_user,
            'partia_cwiczenie' : partia_cwiczenie,
            'partie' : partie}
    return render(request, 'partia_cwiczenia.html', dane)


def cwiczenie (request, id):
    cwiczenie_user = Cwiczenia.objects.get(pk=id)
    partie = Partie.objects.all()
    film = cwiczenie_user.film
    dane = {'cwiczenie_user' : cwiczenie_user, 'partie' : partie, 'film':film}
    return render(request, 'cwiczenia.html', dane)


def kalkulator(request):
    wynik=''
    bialko=''
    wegle=''
    tluszcze=''
    try:
        if request.method=="POST":
            waga = eval(request.POST.get('waga'))
            wzrost = eval(request.POST.get('wzrost'))
            wiek = eval(request.POST.get('wiek'))
            plec=request.POST.get('plec')
            wariant= eval(request.POST.get('wariant'))
            cel = request.POST.get('cel')

            if plec=="M":
                wynik1 = (66.5 + (13.75 * waga) + (5.003 * wzrost) - (6.775 * wiek)) *wariant
                wynik = round(wynik1)
                if cel=="case1":
                    wynik = wynik
                elif cel == "case2":
                    wynik = wynik - 200
                elif cel == "case3":
                    wynik = wynik + 300

            elif plec=="K":
                wynik1 = (665.1 + (9.563 * waga) + (1.85 * wzrost) - (4.676 * wiek)) * wariant
                wynik = round(wynik1)
                if cel=="case1":
                    wynik = wynik
                elif cel == "case2":
                    wynik = wynik - 400
                elif cel == "case3":
                    wynik = wynik + 500
            bialko = round(waga * 1.8)
            wegle = waga * 4
            tluszcze = round(waga * 1.2)
    except:
        wynik = "Podales nieprawidlowa wartosc uzywaj tylko liczb"
    return render(request, 'kalkulator.html', {'wynik': wynik, 'bialko': bialko, 'wegle': wegle, 'tluszcze': tluszcze})


def plan(request):
    nazwa = ''
    opis =''
    try:
        if request.method == "POST":
            dni = request.POST.get('dni')

            if dni == "case1":
                i = Plany.objects.get(pk=1)
                nazwa = i.nazwa
                opis = i.opis
            elif dni == "case2":
                i = Plany.objects.get(pk=2)
                nazwa = i.nazwa
                opis = i.opis
            elif dni == "case3":
                i = Plany.objects.get(pk=3)
                nazwa = i.nazwa
                opis = i.opis

    except:
        nazwa = "blad"
    return render(request, 'plan.html', {'nazwa': nazwa, 'opis': opis})

def progres(request):
    if request.method == "POST":
        form = RekordForm(request.POST)
        if form.is_valid():
            rekord = form.save(commit=False)
            rekord.user = request.user
            rekord.date = date.today()
            rekord.save()
    else:
        form = RekordForm()

    return render(request, 'progres.html', {'form':form} )

def rekordy(request):

    rekordy = Rekordy.objects.all()
    return render(request, 'rekord.html', { 'rekordy': rekordy})

def rekord(request, id):
    rekord = Rekordy.objects.get(pk=id)
    return render(request, 'wynik.html', {'rekord': rekord})
# Create your views here.
