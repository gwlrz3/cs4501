from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.core import serializers
import requests
import urllib.parse

import json


def home(request):

    return render(request, 'home.html')

def hall(request):
    req = requests.get("http://models-api:8000/modelapp/hall/list")
    resp = req.text
    return HttpResponse(resp, content_type='application/json')


def advisor(request):
    req = requests.get("http://models-api:8000/modelapp/advisor/list")
    resp = req.text
    return HttpResponse(resp, content_type='application/json')


def student(request):
    req = urllib.request.Request('http://models-api:8000/modelapp/student/list')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return HttpResponse(resp, content_type='application/json')


def manager(request):
    req = urllib.request.Request('http://models-api:8000/modelapp/manager/list')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return HttpResponse(resp, content_type='application/json')


def room(request):
    req = urllib.request.Request('http://models-api:8000/modelapp/room/list')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return HttpResponse(resp, content_type='application/json')


def lease(request):
    req = urllib.request.Request('http://models-api:8000/modelapp/lease/list')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return HttpResponse(resp, content_type='application/json')