from django.conf.urls import url
from . import views

app_name = 'meeting'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^agenda/(?P<room_id>[0-9]+)/$', views.agenda, name='agenda'),
]
