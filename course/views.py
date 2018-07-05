from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import CourseGroup, GroupMember, CoursePage

def index(request, group_id):
    group = get_object_or_404(CourseGroup, pk=group_id)
    member = GroupMember.objects.filter(group=group)
    return render(request, 'course/group_index.html', {'members': member})

def joingroup(request, group_id):
    if request.user.username != 'Student':
        return render(request, 'course/group_index.html',
                {'errors':["必须是学生才可以加入组"]})
    group = get_object_or_404(CourseGroup, pk=group_id)
    page = CoursePage.objects.get(pk=group.page_id)
    errors = []
    for g in page.group.all():
        m = GroupMember.objects.filter(group=g,number=request.session['schoolid'])
        if (m.count() > 0):
            if (g == group):
                errors = ["你已经在这个组里面了"]
            else:
                errors = ["你在这个课的其他组里"]
    if errors == []:
        m = GroupMember(group=group)
        m.name = request.session['realname']
        m.number = request.session['schoolid']
        m.save()
    member = GroupMember.objects.filter(group=group)
    return render(request, 'course/group_index.html',
            {'members': member,
             'errors': errors})

def leavegroup(request, group_id):
    group = get_object_or_404(CourseGroup, pk=group_id)
    m = GroupMember.objects.filter(group=group,number=request.session['schoolid'])
    if (m.count() > 0):
        m.delete()
    member = GroupMember.objects.filter(group=group)
    return render(request, 'course/group_index.html',
            {'members': member})
