from django.db import models

# Create your models here.
class RegisterInfo(models.Model):
   
    Name = models.CharField(max_length=250)
    Username = models.CharField(max_length=250)
    Email = models.EmailField()
    Password = models.CharField(max_length=250)
    Confirmpassword = models.CharField(max_length=250)