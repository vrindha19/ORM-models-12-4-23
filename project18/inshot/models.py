

from django.db import models

# Create your models here.
class loginInfo(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    # description=models.TextField()
