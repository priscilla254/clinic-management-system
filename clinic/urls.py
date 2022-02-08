from django.urls import path
from .import views
from .views import homePage,DoctorCreate,DoctorUpdateView,DoctorDeleteView,DoctorsList

urlpatterns=[
    path('',homePage.as_view()),
    # path('doctors/',views.DoctorsView,name="patients"),
    path('doctors/',DoctorsList.as_view(),name="doctors"),
    path('patients/',views.PatientsView,name="doctors"),
    path('create_doctor/',DoctorCreate.as_view(),name="add_doctor"),
    path('doctors/<str:pk>/',DoctorUpdateView.as_view(),name="update"),
    path('doctors/<str:pk>/',DoctorDeleteView.as_view(),name='delete'),


]