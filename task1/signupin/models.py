from django.db import models
from django.contrib.auth.models import User

class UTModel(models.Model):
    type=[('Patient','PATIENT'),('Doctor','DOCTOR')]
    usertype=models.CharField(max_length=20,choices=type, default='Patient')

class SignUpModel(User):
    ProfilePic=models.ImageField(upload_to='profilepic/')
    ConfirmPassword=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)







