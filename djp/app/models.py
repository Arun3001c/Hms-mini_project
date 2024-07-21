from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    languages = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'app_doctor'
        
    def __str__(self):
        return self.name

class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    disease = models.CharField(max_length=200)
    appointmentdate = models.DateField()

    def __str__(self):
        return self.name


class AdminCred(models.Model):
    admin_username = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_gender = models.CharField(max_length=10)
    patient_address = models.CharField(max_length=255)
    patient_email = models.EmailField()
    patient_disease = models.CharField(max_length=100)
    patient_mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.patient_name
    
    class Meta:
        db_table = 'app_appointments'
