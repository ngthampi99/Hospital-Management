from django.db import models

# Create your models here.
class Registerdb(models.Model):
    User_Name = models.CharField(max_length=100,null=True,blank=True)
    Email_ID = models.EmailField(null=True,blank=True)
    Mob_No = models.IntegerField(null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)

class Appointmentdb(models.Model):
    Department= models.CharField(max_length=100,null=True,blank=True)
    Doctor = models.CharField(max_length=100,null=True,blank=True)
    DOB = models.CharField(max_length=200,null=True,blank=True)
    Name = models.CharField(max_length=200,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Message = models.TextField(max_length=300,null=True,blank=True)

