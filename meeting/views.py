from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import MeetingRoom, RoomAgenda
from .forms import AgendaForm
from django.urls import reverse

def index(request):
    rooms = MeetingRoom.objects.all()
    if (rooms.count() == 0):
        raise Http404("没有定义会议室")
    if (rooms.count() > 1):
        return render(request, 'meeting/room_index.html', {'rooms': rooms})
    return HttpResponseRedirect(reverse('meeting:agenda_list', args=(rooms.first().id,)))

def agenda_add(request, room_id):
    room = get_object_or_404(MeetingRoom, pk=room_id)
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            agenda = RoomAgenda(room=room)
            agenda.title = form.cleaned_data['note']
            agenda.start_time = form.cleaned_data['start']
            agenda.end_time = form.cleaned_data['end']
            agenda.username = '123'
            if form.cleaned_data['repeatable'] == 1:
                agenda.date = 0 - form.cleaned_data['week']
            else:
                date = form.cleaned_data['date']
                agenda.date = date.year * 10000 + date.month * 100 + date.day
            agenda.save()
            return HttpResponseRedirect(reverse('meeting:agenda_list', args=(room.id,)))
    else:
        form = AgendaForm()
    return render(request, 'meeting/agenda_add.html', {'form': form})

def agenda_list(request, room_id):
    room = get_object_or_404(MeetingRoom, pk=room_id)
    agendas = RoomAgenda.objects.filter(room=room)
    return render(request, 'meeting/agenda_list.html', {'agendas': agendas})

def agenda_view(request, agenda_id):
    agenda = get_object_or_404(RoomAgenda, pk=agenda_id)
    return render(request, 'meeting/agenda_view.html', {'agenda': agenda})

def agenda_del(request, agenda_id):
    agenda = get_object_or_404(RoomAgenda, pk=agenda_id)
    room = agenda.room
    agenda.delete()
    return HttpResponseRedirect(reverse('meeting:agenda_list', args=(room.id,)))
