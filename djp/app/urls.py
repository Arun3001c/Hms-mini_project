from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('appointment/', appointment, name='appointment'),
    path('contact/', contact, name='contact'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),    
    path('doctors/', doctor_list_view, name='doctor_list'),
    path('admins/', admin_list_view, name='admin_list'),
    path('patients/', patient_list_view, name='patient_list'),
    path('appointments/', appointment_list_view, name='appointment_list'),
    path('add_appointment/', add_appointment, name='add_appointment'),
    path('add_doctor/', add_doctor, name='add_doctor'),
    path('create_patient/', add_patient, name='add_patient'),
    path('add_admin/', add_admin, name='add_admin'),
]
