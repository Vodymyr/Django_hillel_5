from django.shortcuts import render
from myapp.models import Teacher


def teachers_list(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teachers_list.html', context)
