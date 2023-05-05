from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, AddStudentToGroupView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
    path('add_to_group/<int:pk>/', AddStudentToGroupView.as_view(), name='add_student_to_group'),
]
