from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import MeetingRoom

def index(request):
    rooms = MeetingRoom.objects.all()
    if (rooms.count() == 0):
        raise Http404("没有定义会议室")
#    if (rooms.count() > 1):
    return render(request, 'meeting/room_index.html', {'rooms': rooms})
