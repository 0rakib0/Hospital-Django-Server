from django.urls import path
from . import views


urlpatterns = [
    path('payments/', views.Payments.as_view(), name='payemnts'),
    path('payments/<userId>/', views.Payments.as_view(), name='payemnts'),
    path('appoinment/', views.Appoinment.as_view(), name='appoinment'),
    path('appoinment/<int:id>/', views.Appoinment.as_view(), name='appoinment'),
    path('patients-appoinment/<patientsId>/', views.PatientsAppoinmnet, name='patients_appoinment'),
    path('notise/', views.NotiseView.as_view(), name='notise_view')
]