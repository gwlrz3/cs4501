from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from modelapp import models
from modelapp import forms
import json
from django.conf import settings
import os
import hmac
import datetime


def hall_list(request):
    data = models.Hall.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


def hall_create(request):
    form = forms.HallForm(json.loads(request.body.decode()))
    if form.is_valid():
        form.save()
    return redirect('hall/list')


def hall_delete(request, pk):
    hall = get_object_or_404(models.Hall, pk=pk)
    if request.method == 'POST':
        hall.delete()
    return redirect('hall/list')


def hall_update(request, pk):
    hall = get_object_or_404(models.Hall, pk=pk)
    form = forms.HallForm(json.loads(request.body.decode()), instance = hall)
    if form.is_valid():
        form.save()
    return redirect('hall/list')


def advisor_list(request):
    data = models.Advisor.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


def advisor_create(request):
    form = forms.AdvisorForm(json.loads(request.body.decode()))
    if form.is_valid():
        form.save()
    return redirect('advisor/list')


def advisor_delete(request, pk):
    advisor = get_object_or_404(models.Advisor, pk=pk)
    if request.method == 'POST':
        advisor.delete()
    return redirect('advisor/list')


def advisor_update(request, pk):
    advisor = get_object_or_404(models.Advisor, pk=pk)
    form = forms.AdvisorForm(json.loads(request.body.decode()), instance = advisor)
    if form.is_valid():
        form.save()
    return redirect('advisor/list')


def student_list(request):
    data = models.Student.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


def student_create(request):
    form = forms.StudentForm(json.loads(request.body.decode()))
    if form.is_valid():
        form.save()
    return redirect('student/list')


def student_delete(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    if request.method == 'POST':
        student.delete()
    return redirect('student/list')


def student_update(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    form = forms.StudentForm(json.loads(request.body.decode()), instance = student)
    if form.is_valid():
        form.save()
    return redirect('student/list')


def manager_list(request):
    data = models.Manager.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


def manager_create(request):
    form = forms.ManagerForm(json.loads(request.body.decode()))
    if form.is_valid():
        form.save()
    return redirect('manager/list')


def manager_delete(request, pk):
    manager = get_object_or_404(models.Manager, pk=pk)
    if request.method == 'POST':
        manager.delete()
    return redirect('manager/list')


def manager_update(request, pk):
    manager = get_object_or_404(models.Manager, pk=pk)
    form = forms.ManagerForm(json.loads(request.body.decode()), instance = manager)
    if form.is_valid():
        form.save()
    return redirect('manager/list')


def room_list(request):
    data = models.Room.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


def room_create(request):
    form = forms.RoomForm(json.loads(request.body.decode()))
    if form.is_valid():
        form.save()
    return redirect('room/list')


def room_delete(request, pk):
    room = get_object_or_404(models.Room, pk=pk)
    if request.method == 'POST':
        room.delete()
    return redirect('room/list')


def room_update(request, pk):
    room = get_object_or_404(models.Room, pk=pk)
    form = forms.RoomForm(json.loads(request.body.decode()), instance = room)
    if form.is_valid():
        form.save()
    return redirect('room/list')


def lease_list(request):
    data = models.Lease.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


def lease_create(request):
    form = forms.LeaseForm(json.loads(request.body.decode()))
    if form.is_valid():
        form.save()
    return redirect('lease/list')


def lease_delete(request, pk):
    lease = get_object_or_404(models.Lease, pk=pk)
    if request.method == 'POST':
        lease.delete()
    return redirect('lease/list')


def lease_update(request, pk):
    lease = get_object_or_404(models.Lease, pk=pk)
    form = forms.LeaseForm(json.loads(request.body.decode()), instance = lease)
    if form.is_valid():
        form.save()
    return redirect('lease/list')


def user_create(request):
    form = forms.UserForm(json.loads(request.body.decode()))
    # 这里就要加"用户名已存在"的判断，不存在重复用户名返回1，存在返回-1
    if form.is_valid():
        form.save()
        response = {
            "res_code": 1,
            "res_message": "registration succeeds"
            }
        return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        response = {
            "res_code": -1,
            "res_message": "registration fails"
            }
        return HttpResponse(json.dumps(response), content_type='application/json')


def user_list(request):
    data = models.User.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


def user_authenticate(request):
    form = forms.UserForm(json.loads(request.body.decode()))
    if not form.is_valid():
        response = {
            "res_code": '-1',
            "res_message": 'Wrong format of username/password'
            }
        return HttpResponse(response, content_type='application/json')

    user = get_object_or_404(models.User, username = form.cleaned_data['username'])

    if user.password == form.cleaned_data['password']:
        response = {
            "res_code": '1',
            "res_message": 'authentication succeeds'
            }
        return HttpResponse(response, content_type='application/json')
    else:
        response = {
            "res_code": '-1',
            "res_message": 'Wrong password'
            }
        return HttpResponse(response, content_type='application/json')


def authenticator_create(request):
    data = json.loads(request.body.decode("utf-8"))
    user = get_object_or_404(models.User, username=data["username"])
    uid = user.username

    auth = hmac.new(
        key=settings.SECRET_KEY.encode('utf-8'),
        msg=os.urandom(32),
        digestmod='sha256',
    ).hexdigest()

    date = datetime.datetime.now()

    auth_form = forms.AuthenticatorForm({
        "authenticator": auth,
        "user": uid,
        "date_created": date
    })

    if auth_form.is_valid():
        auth_form.save()
        response = {
            "res_code": 1,
            "res_message": 'authenticator created',
            "authenticator": auth
        }
    else:
        response = {
            "res_code": -1,
            "res_message": 'authenticator creation fails',
            "authenticator": 'what'
        }

    return HttpResponse(json.dumps(response), content_type='application/json')


def authenticator_delete(request, authenticator):
    auth = get_object_or_404(models.Authenticator, pk=authenticator)
    if request.method == 'POST':
        auth.delete()


def listing_create(request):
    form = forms.ListingForm(json.loads(request.body.decode()))
    if form.is_valid():
        form.save()


    

