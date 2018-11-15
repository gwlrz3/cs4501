from django.shortcuts import render, redirect, get_object_or_404, render_to_response, reverse
from django.http import HttpResponse, HttpRequest
from django.core import serializers
import requests
import urllib.parse
from .forms import LoginForm, RegisterForm, RoomForm
from . import views
import json


def home(request):
    auth = request.COOKIES.get('auth')

    if auth:
        res = requests.post("http://exp-api:8000/expapp/read_user", json={"authenticator": auth})
        res = res.json()
        return render(request, 'home.html', {'username': res["username"]})

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

    auth = request.COOKIES.get('auth')

    if auth:
        res = requests.post("http://exp-api:8000/expapp/read_user", json={"authenticator": auth})
        res = res.json()
        username = res["username"]

    return render(request, 'room.html', {'objects': data, 'username': username})


def room_add(request):
    auth = request.COOKIES.get('auth')

    if auth is None:
        return redirect('/webapp/login?next=info/room')

    form = RoomForm(request.POST)
    # check whether it's valid:
    if not form.is_valid():
        return redirect('/webapp/home')

    hall_no = form.cleaned_data["hall"]
    room_no = form.cleaned_data["room_no"]
    price = form.cleaned_data["price"]

    resp = requests.post("http://exp-api:8000/expapp/add/room", json={
        "hall": hall_no,
        "room_no": room_no,
        "price": price
    })

    resp = resp.json()

    if resp["res_code"] == 0:
        return redirect('webapp/info/room')

    return redirect('/webapp/info/room')


def lease(request):
    req = requests.get("http://exp-api:8000/expapp/showall/lease")
    data = req.json()
    return render(request, 'lease.html', {'objects': data})


def login(request):
    if request.method == 'GET':
        # next = request.GET.get('next')
        return render(request, 'login.html')

    form = LoginForm(request.POST)
    # check whether it's valid:
    if not form.is_valid():
        return render(request, 'login.html')

    username = form.cleaned_data["username"]
    password = form.cleaned_data["password"]

    res = requests.post("http://exp-api:8000/expapp/login", json={
        "username": username,
        "password": password
    })

    res = res.json()
    # next = form.cleaned_data.get('next')

    if res['res_code'] == 1:
        response = redirect('/home', {'username': username})

        # if next is not None:
        #     response = redirect('webapp/' + str(next))

        response.set_cookie("auth", res["authenticator"])
        return response

    return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

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

    res = res.json()

    if res['res_code'] == 1:
        response = render_to_response('home.html', {'username': username})
        response.set_cookie("auth", res["authenticator"])
        return response

    return render(request, 'register.html')


def logout(request):
    auth = request.COOKIES.get('auth')
    resp = requests.post("http://exp-api:8000/expapp/logout", json={"authenticator": auth})
    resp = resp.json()
    if resp['res_code'] == 1:
        response = render_to_response('home.html')
        response.delete_cookie("auth")
        return response

    return render(request, 'home.html')


def search(request):

    form = SearchForm(request.POST)
    # check whether it's valid:
    if not form.is_valid():
        return redirect('/home')

    keyword = form.cleaned_data["keyword"]

    resp = requests.post("http://exp-api:8000/expapp/add/room", json={
        "hall": hall_no,
        "room_no": room_no,
        "price": price
    })

    resp = resp.json()

    if resp["res_code"] == 0:
        return redirect('webapp/info/room')

    return redirect('/webapp/info/room')
