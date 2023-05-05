from django.urls import path
from myapp.views import teachers_list

urlpatterns = [
    path('teachers', teachers_list, name='teachers_list'),
]
