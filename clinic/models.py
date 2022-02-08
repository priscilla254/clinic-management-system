from django.db import models


specialties=(
    ('dentist','dentist'),
    ('optician','optician'),
    ('chiropractor','chiropractor'),
    ('dermatologist','dermatologist'),
)

class Doctors(models.Model):
    name=models.CharField(max_length=80,blank=True)
    specialty=models.CharField(choices=specialties,max_length=80)
    def __str__(self):
        return f"("+self.name+ ', '+self.specialty+")"
    pass   

class Patients(models.Model):
    name=models.CharField(max_length=100)
    admission_date=models.DateTimeField(auto_now_add=True)
    doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    condition=models.TextField()
    def __str__(self):
        return self.name