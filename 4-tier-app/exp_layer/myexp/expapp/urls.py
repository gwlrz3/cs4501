from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'expapp'
urlpatterns = [
    url(r'showall/hall', views.allHall, name='allHall'),
    url(r'showall/advisor', views.allAdvisor, name='allAdvisor'),
    url(r'showall/student', views.allStudent, name='allStudent'),
    url(r'showall/manager', views.allManager, name='allManager'),
    url(r'showall/room', views.allRoom, name='allRoom'),
    url(r'showall/room/sorted', views.allRoom, name='sortedRoom'),
    url(r'showall/lease', views.allLease, name='allLease'),

    url(r'add/room', views.addRoom, name='addRoom'),


    url(r'register', views.register, name='register'),
    url(r'login', views.login, name='login'),
    url(r'read_user', views.read_user, name='read_user'),
    url(r'logout', views.logout, name='logout')



]
