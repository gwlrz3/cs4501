from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'webapp'
urlpatterns = [

    url(r'home/', views.home, name='home'),

    url(r'info/hall', views.hall, name='hall'),
    url(r'info/advisor', views.advisor, name='advisor'),
    url(r'info/student', views.student, name='student'),
    url(r'info/manager', views.manager, name='manager'),
    url(r'info/room', views.room, name='room'),
    url(r'info/lease', views.lease, name='lease'),
    url(r'login_page', views.login_page, name='login_page'),
    url(r'register_page', views.register_page, name='register_page'),
    url(r'login', views.login, name='login'),
    url(r'register', views.register, name='register'),

]

