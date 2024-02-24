from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.Doctors.as_view(), name='doctors'),
]
