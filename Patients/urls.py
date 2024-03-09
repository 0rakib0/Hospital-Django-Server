from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patientsList.as_view(), name='patients'),
    path('patients/<int:id>/', views.patientsList.as_view(), name='patients_update'),
    path('discharge-patients/', views.dischargePatients, name='discharge_patients'),
    path('in-treatment-patients/', views.inTreatment, name='intreatment_patients'),
    path('single-patient/<str:email>/', views.singlePatientsInfo, name='patientsInfo'),
]
