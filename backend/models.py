from django.db import models

# Create your models here.

class Departmentdb(models.Model):

    Dept_Name = models.CharField(max_length=100,null=True,blank=True)
    Description = models.TextField(max_length=200,null=True,blank=True)
    Image = models.ImageField(upload_to="Department",null=True,blank=True)

class Doctordb(models.Model):
    Dept_Name = models.CharField(max_length=100, null=True, blank=True)
    Doctor_Name = models.CharField(max_length=100,null=True,blank=True)
    Description = models.TextField(max_length=200, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Expertise_Field =models.TextField(max_length=200, null=True, blank=True)
    Doc_Image = models.ImageField(upload_to="Doctor", null=True, blank=True)




