from django.conf.urls import url
from . import views

app_name = 'course'
urlpatterns = [
    url(r'^join/(?P<group_id>[0-9]+)/$', views.joingroup, name='joingroup'),
    url(r'^leave/(?P<group_id>[0-9]+)/$', views.leavegroup, name='leavegroup'),
    url(r'(?P<group_id>[0-9]+)/$', views.index, name='index'),
]
