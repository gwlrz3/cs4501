from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.core import serializers
import requests
import urllib.parse

import json


# def most_expensive_rooms(request):
#     data = models.Room.objects.all()
#     data_json = serializers.serialize('json', data)


def allHall(request):
    req = requests.get("http://models-api:8000/modelapp/hall/list")
    resp = req.text
    return HttpResponse(resp, content_type='application/json')


def allAdvisor(request):
    req = requests.get("http://models-api:8000/modelapp/advisor/list")
    resp = req.text
    return HttpResponse(resp, content_type='application/json')


def allStudent(request):
    req = requests.get("http://models-api:8000/modelapp/student/list")
    resp = req.text
    return HttpResponse(resp, content_type='application/json')


def allManager(request):
    req = requests.get("http://models-api:8000/modelapp/manager/list")
    resp = req.text
    return HttpResponse(resp, content_type='application/json')


def allRoom(request):
    req = requests.get("http://models-api:8000/modelapp/room/list")
    resp = req.text
    return HttpResponse(resp, content_type='application/json')


def allLease(request):
    req = requests.get("http://models-api:8000/modelapp/lease/list")
    resp = req.text
    return HttpResponse(resp, content_type='application/json')