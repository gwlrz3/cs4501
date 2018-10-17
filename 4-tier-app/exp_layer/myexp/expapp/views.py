from django.shortcuts import render
from django.db.models.expressions import RawSQL, OrderBy

from model_layer.modelapp import models

def most_expensive_rooms(request):
	data = models.Room.objects.all().order_by(OrderBy(RawSQL("cast(data->>%s as integer)", ("price",)), descending=True))
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


def hall_list(request):
	data = models.Hall.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')

def advisor_list(request):
    data = models.Advisor.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')

def student_list(request):
    data = models.Student.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')

def manager_list(request):
    data = models.Manager.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')

def room_list(request):
    data = models.Room.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')

def lease_list(request):
    data = models.Lease.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')