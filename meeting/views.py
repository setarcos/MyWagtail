from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import MeetingRoom
from .forms import AgendaForm
from django.urls import reverse

def index(request):
    rooms = MeetingRoom.objects.all()
    if (rooms.count() == 0):
        raise Http404("没有定义会议室")
    if (rooms.count() > 1):
        return render(request, 'meeting/room_index.html', {'rooms': rooms})
    return HttpResponseRedirect(reverse('meeting:agenda', args=(rooms.first().id,)))

def agenda(request, room_id):
    room = get_object_or_404(MeetingRoom, pk=room_id)
    if request.method == 'POST':
        form = AgendaForm(request.POST)
    else:
        form = AgendaForm()
    return render(request, 'meeting/agenda_list.html', {'form': form})
