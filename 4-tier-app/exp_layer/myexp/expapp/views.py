from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.core import serializers
import requests
import urllib.parse

from kafka import KafkaProducer
from elasticsearch import Elasticsearch
import json
import time


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
        #if succeed, post data to kafka
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        data['id'] = resp['id']
        producer.send('newListing', json.dumps(data).encode('utf-8'))
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

def search(request):
    queryBody = json.loads(request.body.decode("utf-8"))
    es = Elasticsearch(['es'])

    #if index does not exist in es, inject data from database into es for searching
    if not es.indices.exists('listing_index'):
        resp = requests.get("http://models-api:8000/modelapp/room/list")
        resp = resp.json()
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        for ele in resp:
            room = {
                'id' : ele['pk'],
                'hall' : ele['fields']['hall'],
                'room_no' : ele['fields']['room_no'],
                'price' : ele['fields']['price'],
            }
            producer.send('newListing', json.dumps(room).encode('utf-8'))

    #loop until search succeeds
    success = False
    while not success:
        try:
            result = es.search(index='listing_index', body={'query': {'query_string': {'query': queryBody["keyword"]}}})
            success = True
            break
        except:
            time.sleep(5)
            success = False
    return HttpResponse(json.dumps(result), content_type='application/json')







