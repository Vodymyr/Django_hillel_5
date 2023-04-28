from django.shortcuts import render, redirect
from .models import Teacher, Group
from .forms import TeacherForm, GroupForm

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers_list')
    else:
        form = TeacherForm()
    context = {'form': form}
    return render(request, 'teacher_form.html', context)


def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups_list')
    else:
        form = GroupForm()
    context = {'form': form}
    return render(request, 'group_form.html', context)


def teachers_list(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teachers_list.html', context)


def groups_list(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'groups_list.html', context)
