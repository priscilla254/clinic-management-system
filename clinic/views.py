
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import *
from django.views.generic.edit import CreateView,DeleteView,UpdateView
class homePage(TemplateView):
    template_name='home.html'


def PatientsView(request):
    patient_list=Patients.objects.all()
    context={'patient_list':patient_list}
    return render(request,'patients.html',context)

# def DoctorsView(request):
#     doctor_list=Doctors.objects.all()
#     context={'doctor_list':doctor_list}
#     return render(request,'doctors.html',context)

class DoctorsList(ListView):
    model=Doctors
    fields=['name','specialty','pk',]
    context_object_name='doctor_list'
    template_name='doctors.html'

# CRUD operations using class-based views
class DoctorCreate(CreateView):
    model=Doctors
    fields=['name','specialty']
    template_name="create_doctor.html"

class DoctorUpdateView(UpdateView):
    model=Doctors
    fields=' __all__'
    template_name="create_doctor.html"

class DoctorDeleteView(DeleteView):
    model=Doctors
    success_url=reverse_lazy('doctors')
    template_name="doctor_confirm_delete.html"