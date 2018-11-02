from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.core import serializers
import requests
import urllib.parse


import json


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


def addRoom(request):
    data = json.loads(request.body.decode("utf-8"))
    resp = requests.post("http://models-api:8000/modelapp/room/create", json=data)

    resp = resp.json()

    if resp["res_code"] == 1:
        return HttpResponse(json.dumps(resp), content_type='application/json')
    else:
        return HttpResponse(json.dumps({
            "res_code": 0,
            "res_message": "Room Create Fails"
        }), content_type='application/json')


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
    data = json.loads(request.body.decode("utf-8"))
    resp1 = requests.post("http://models-api:8000/modelapp/user/create", json=data)

    resp1 = resp1.json()
    # 这里的判断是用户名是否重复，写入是否成功，成功了搞authenticator
    if resp1["res_code"] == 1:
        resp2 = requests.post("http://models-api:8000/modelapp/authenticator/create", json=data)
        resp2 = resp2.json()

        return HttpResponse(json.dumps(resp2), content_type='application/json')
    else:
        return HttpResponse(json.dumps(resp1), content_type='application/json')


def login(request):
    data = json.loads(request.body.decode("utf-8"))

    resp1 = requests.post("http://models-api:8000/modelapp/user/authenticate", json=data)
    resp1 = resp1.json()

    if resp1["res_code"] == 1:
        resp2 = requests.post("http://models-api:8000/modelapp/authenticator/create", json=data)
        resp2 = resp2.json()
        return HttpResponse(json.dumps(resp2), content_type='application/json')
    else:
        return HttpResponse(json.dumps(resp1), content_type='application/json')


def read_user(request):
    data = json.loads(request.body.decode("utf-8"))
    resp = requests.post("http://models-api:8000/modelapp/authenticator/read_user", json=data)

    return HttpResponse(resp, content_type='application/json')


def logout(request):
    data = json.loads(request.body.decode("utf-8"))
    resp = requests.post("http://models-api:8000/modelapp/authenticator/delete", json=data)
    return HttpResponse(resp, content_type='application/json')




