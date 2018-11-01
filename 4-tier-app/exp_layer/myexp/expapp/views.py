from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.core import serializers
import requests
import urllib.parse


import json
from mymodel.modelapp import forms


# def most_expensive_rooms(request):
# 	data = models.Room.objects.all().order_by(OrderBy(RawSQL("cast(data->>%s as integer)", ("price",)), descending=True))
#     data_json = serializers.serialize('json', data)
#     return HttpResponse(data_json, content_type='application/json')


def allHall(request):
    resp = requests.get("http://models-api:8000/modelapp/hall/list")
    resp = resp.text
    return HttpResponse(resp, content_type='application/json')


def allAdvisor(request):
    resp = requests.get("http://models-api:8000/modelapp/advisor/list")
    resp = resp.text
    return HttpResponse(resp, content_type='application/json')


def allStudent(request):
    resp = requests.get("http://models-api:8000/modelapp/student/list")
    resp = resp.text
    return HttpResponse(resp, content_type='application/json')


def allManager(request):
    resp = requests.get("http://models-api:8000/modelapp/manager/list")
    resp = resp.text
    return HttpResponse(resp, content_type='application/json')


def allRoom(request):
    resp = requests.get("http://models-api:8000/modelapp/room/list")
    resp = resp.text
    return HttpResponse(resp, content_type='application/json')


def sortedRoom(request):
    resp = requests.get("http://models-api:8000/modelapp/room/list")
    room_json = resp.json()
    sorted_room = sorted(room_json, key=lambda x: x['fields']['price'], reverse=True)
    return HttpResponse(json.dumps(sorted_room), content_type='application/json')


def allLease(request):
    resp = requests.get("http://models-api:8000/modelapp/lease/list")
    resp = resp.text
    return HttpResponse(resp, content_type='application/json')

def register(request):
    form = forms.UserForm(json.loads(request.body.decode()))
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    resp1 = requests.post("http://models-api:8000/modelapp/user/create", json = {
        'username' : username,
        'password' : password,
    })
    resp1 = resp1.json()

    if resp1['res_code'] == 1:
        resp2 = requests.post("http://models-api:8000/modelapp/authenticator/create", json = {
        'username' : username,
        'password' : password,
        })
        resp2 = resp2.json()
        return HttpResponse(resp2, content_type='application/json')
    else:
        response = {
            'res_code' : '-1',
            'res_message' : 'authenticator creation fails',
            'authenticator' : ''
        }
        return HttpResponse(response, content_type='application/json')
    
    


def login(request):

def logout(request):

def createListing(request):

