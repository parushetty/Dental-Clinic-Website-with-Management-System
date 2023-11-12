from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
    path("", views.index, name='homepage'),
    path('appointment.html', views.appointment_form, name='appointment_form'),
    path('appointment_success.html', views.appointment_success, name='appointment_success'),
    path('DENTAL TOURISM.html', views.dental_tourism, name='dental_tourism'),
    path('admin/login/', CustomLoginView.as_view(), name='admin_login'),
   
]

