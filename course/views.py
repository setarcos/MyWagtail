from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import CourseGroup, GroupMember, CoursePage

@login_required
def index(request, group_id):
    group = get_object_or_404(CourseGroup, pk=group_id)
    member = GroupMember.objects.filter(group=group)
    return render(request, 'course/group_index.html', {'members': member})

@login_required
def joingroup(request, group_id):
    group = get_object_or_404(CourseGroup, pk=group_id)
    page = CoursePage.objects.get(pk=group.page_id)
    errors = []
    for g in page.group.all():
        m = GroupMember.objects.filter(group=g,number="123")
        if (m.count() > 0):
            if (g == group):
                errors = ["你已经在这个组里面了"]
            else:
                errors = ["你在这个课的其他组里"]
    if errors == []:
        m = GroupMember(group=group)
        m.name = "杨"
        m.number = '123'
        m.save()
    member = GroupMember.objects.filter(group=group)
    return render(request, 'course/group_index.html',
            {'members': member,
             'errors': errors})

@login_required
def leavegroup(request, group_id):
    group = get_object_or_404(CourseGroup, pk=group_id)
    m = GroupMember.objects.filter(group=group,number="123")
    if (m.count() > 0):
        m.delete()
    member = GroupMember.objects.filter(group=group)
    return render(request, 'course/group_index.html',
            {'members': member})
