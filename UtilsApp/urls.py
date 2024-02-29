from django.urls import path
from . import views


urlpatterns = [
    path('payments/', views.Payments.as_view(), name='payemnts'),
    path('payments/<userId>/', views.Payments.as_view(), name='payemnts'),
    path('appoinment/', views.Appoinment.as_view(), name='appoinment'),
    path('appoinment/<pId>/', views.Appoinment.as_view(), name='appoinment'),
]