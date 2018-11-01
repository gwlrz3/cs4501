from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.core import serializers
import requests
import urllib.parse
from .forms import LoginForm

import json


def home(request):

    return render(request, 'home.html')


def hall(request):
    req = requests.get("http://exp-api:8000/expapp/showall/hall")
    data = req.json()
    return render(request, 'hall.html', {'objects': data})


def advisor(request):
    req = requests.get("http://exp-api:8000/expapp/showall/advisor")
    data = req.json()
    return render(request, 'advisor.html', {'objects': data})


def student(request):
    req = requests.get("http://exp-api:8000/expapp/showall/student")
    data = req.json()
    return render(request, 'student.html', {'objects': data})


def manager(request):
    req = requests.get("http://exp-api:8000/expapp/showall/manager")
    data = req.json()
    return render(request, 'manager.html', {'objects': data})


def room(request):
    req = requests.get("http://exp-api:8000/expapp/showall/room")
    data = req.json()
    return render(request, 'room.html', {'objects': data})


def lease(request):
    req = requests.get("http://exp-api:8000/expapp/showall/lease")
    data = req.json()
    return render(request, 'lease.html', {'objects': data})


def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    return render(request, 'register.html')


def login(request):
    # If we received a GET request instead of a POST request
    if request.method == 'GET':
        # display the login form page
        next = request.GET.get('next') or reverse('home')
        return render('login.html', ...)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def register(request):
    # If we received a GET request instead of a POST request
    if request.method == 'GET':
        # display the login form page
        next = request.GET.get('next') or reverse('home')
        return render('login.html', ...)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})