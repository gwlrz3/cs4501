from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
	url(r'hall/list', views.hall_list, name='hall_list'),
	url(r'hall/create', views.hall_create, name='hall_create'),
	url(r'hall/update/(?P<pk>\d+)$', views.hall_update, name='hall_update'),
	url(r'hall/delete/(?P<pk>\d+)$', views.hall_delete, name='hall_delete'),

	url(r'advisor/list', views.advisor_list, name='advisor_list'),
	url(r'advisor/create', views.advisor_create, name='advisor_create'),
	url(r'advisor/update/(?P<pk>\d+)$', views.advisor_update, name='advisor_update'),
	url(r'advisor/delete/(?P<pk>\d+)$', views.advisor_delete, name='advisor_delete'),

	url(r'student/list', views.student_list, name='student_list'),
	url(r'student/create', views.student_create, name='student_create'),
	url(r'student/update/(?P<pk>\d+)$', views.student_update, name='student_update'),
	url(r'student/delete/(?P<pk>\d+)$', views.student_delete, name='student_delete'),

	url(r'manager/list', views.manager_list, name='manager_list'),
	url(r'manager/create', views.manager_create, name='manager_create'),
	url(r'manager/update/(?P<pk>\d+)$', views.manager_update, name='manager_update'),
	url(r'manager/delete/(?P<pk>\d+)$', views.manager_delete, name='manager_delete'),

	url(r'room/list', views.room_list, name='room_list'),
	url(r'room/create', views.room_create, name='room_create'),
	url(r'room/update/(?P<pk>\d+)$', views.room_update, name='room_update'),
	url(r'room/delete/(?P<pk>\d+)$', views.room_delete, name='room_delete'),

	url(r'lease/list', views.lease_list, name='lease_list'),
	url(r'lease/create', views.lease_create, name='lease_create'),
	url(r'lease/update/(?P<pk>\d+)$', views.lease_update, name='lease_update'),
	url(r'lease/delete/(?P<pk>\d+)$', views.lease_delete, name='lease_delete'),

]

# urlpatterns = patterns('myapp.views',
#         url(r'^mymodel/create/$', view='mymodel_create',  name='mymodel_create'),
# )

# urlpatterns += patterns('django.views.generic',
#         url(r'^(?P<model>\w+)/create/$','create_update.create_object', name='object_create'),
#         url(r'^(?P<model>\w+)/(?P<id>\d+)/update/$', 'create_update.update_object', name='object_update' ),
#         url(r'^(?P<model>\w+)/(?P<id>\d+)/delete/$', 'create_update.delete_object', name='object_delete'),        
#         url(r'^(?P<model>\w+)/(?P<object_id>\d+)/$', 'list_detail.object_detail',  name='object_detail'),
#         url(r'^(?P<model>\w+)/$','list_detail.object_list', name='object_list'),
# )

# urlpatterns = [
#     url(r'^(?P<model>\w+)/(?P<object_id>\d+)/$', 'my_app.views.my_object_detail',  name='object_detail'),
# ]

