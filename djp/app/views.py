from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AdminCred, Doctor, Patient, Appointment
import json
from .forms import *
def index(request):
    return render(request, 'myapp/index.html')

def gallery(request):
    return render(request, 'myapp/gallery.html')

def about(request):
    return render(request, 'myapp/about.html')

def appointment(request):
    return render(request, 'myapp/appointment.html')

def contact(request):
    return render(request, 'myapp/contact.html')


def doctor_list_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'myapp/doctor_list.html', {'doctors': doctors})

def admin_list_view(request):
    admins = AdminCred.objects.all()
    return render(request, 'myapp/admins_list.html', {'admins': admins})

def patient_list_view(request):
    patients = Patient.objects.all()
    return render(request, 'myapp/patient_list.html', {'patients': patients})

def appointment_list_view(request):
    appointments = Appointment.objects.all()
    return render(request, 'myapp/appointment_list.html', {'appointments': appointments})


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorApplicationForm()
    return render(request, 'myapp/add_doctor.html', {'form': form})

def add_patient(request):
    if request.method == 'POST':
        form = PatientAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientAppointmentForm()
    return render(request, 'myapp/add_patient.html', {'form': form})

def add_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_list')
    else:
        form = AdminForm()
    return render(request, 'myapp/add_admin.html', {'form': form})

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AppointmentForm()
    return render(request, 'myapp/add_appointment.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)
            admin_username = data.get('admin_username')
            admin_password = data.get('admin_password')

            if admin_username and admin_password:
                try:
                    admin = AdminCred.objects.get(admin_username=admin_username, admin_password=admin_password)
                    if admin:
                        return JsonResponse({'success': True, 'redirect': '/dashboard/'})
                except AdminCred.DoesNotExist:
                    return JsonResponse({'message': 'Invalid username or password'}, status=401)
            else:
                return JsonResponse({'message': 'Username and password required'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)
    elif request.method == 'GET':
        return render(request, 'myapp/login.html')
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

def dashboard(request):
    return render(request, 'myapp/dashboard.html')

