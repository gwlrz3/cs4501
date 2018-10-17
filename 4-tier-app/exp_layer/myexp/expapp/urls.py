from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'hall/list', views.hall_list, name='hall_list'),
	url(r'advisor/list', views.advisor_list, name='advisor_list'),
	url(r'student/list', views.student_list, name='student_list'),
	url(r'manager/list', views.manager_list, name='manager_list'),
	url(r'room/list', views.room_list, name='room_list'),
	url(r'lease/list', views.lease_list, name='lease_list'),

	url(r'room/mostExpensive', views.most_expensive_rooms, name='room_order'),
]
