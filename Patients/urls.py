from django.urls import path
from . import views

urlpatterns = [
    path('add-patients/', views.Patients.as_view(), name='patients')
]
