from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpRequest
from django.core import serializers
import requests
import urllib.parse
from .forms import LoginForm, RegisterForm

import json


def home(request):
    auth = request.COOKIES.get('auth')

    if auth:


        return render(request, 'home.html', {'username': username})

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

    return render(request, 'name.html')


def register(request):

    form = RegisterForm(request.POST)
    # check whether it's valid:
    if not form.is_valid():
        return render(request, 'register.html')

    username = form.cleaned_data["username"]
    password = form.cleaned_data["password"]

    res = requests.post("http://exp-api:8000/expapp/register", json={
        "username": username,
        "password": password
    })

    res_json = res.json()

    if res_json['res_code'] == 1:
        response = render_to_response('home.html', {'username': username})
        response.set_cookie("auth", res_json["authenticator"])
        return response

    return render(request, 'register.html')

