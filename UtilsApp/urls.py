from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('payments/', views.Payments.as_view(), name='payemnts'),
    path('payments/<userId>/', views.Payments.as_view(), name='payemnts'),
    path('appoinment/', views.Appoinment.as_view(), name='appoinment'),
    path('appoinment/<int:id>/', views.Appoinment.as_view(), name='appoinment'),
    path('update-appoinment-status/<int:id>/', views.UpdateAppoinemntStatus, name='update_apooinment_status'),
    path('filter-appoinment-data/', views.FilterAppoinment, name='filter_appoinment_data'),
    path('patients-appoinment/<patientsId>/', views.PatientsAppoinmnet, name='patients_appoinment'),
    path('notice/', views.NotiseView.as_view(), name='notice'),
    path('notice/<int:id>/', views.NotiseView.as_view(), name='notice'),
    path('messages/', views.MessageView.as_view(), name='message'),
    path('messages/<int:id>/', views.MessageView.as_view(), name='message')
]