from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patientsList.as_view(), name='patients')
]
