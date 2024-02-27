from django.urls import path
from . import views


urlpatterns = [
    path('payments/', views.Payments.as_view(), name='payemnts')
]