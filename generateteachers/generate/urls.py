from django.urls import path
from .views import teacher_create, group_create, teachers_list, groups_list

urlpatterns = [
    path('teacher/', teacher_create, name='teacher_create'),
    path('teachers/', teachers_list, name='teachers_list'),
    path('group/', group_create, name='group_create'),
    path('groups/', groups_list, name='groups_list'),
]
