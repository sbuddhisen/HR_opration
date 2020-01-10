from django.db import models

# Create your models here.
class HR_Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=20)
    company_name =models.CharField(max_length=100,primary_key=True)



class Applicant_Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True,max_length=60)
    # username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)


class Manager_Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True,max_length=60)
    # username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)

class Interviewer_Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True,max_length=60)
    # username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)

class Job_Details(models.Model):
    name = models.CharField(max_length=100)
    hr_email = models.EmailField()
    comp_name = models.CharField(max_length=100)