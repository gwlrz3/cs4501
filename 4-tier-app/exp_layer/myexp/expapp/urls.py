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
    url(r'showall/lease', views.allLease, name='allLease'),

]
