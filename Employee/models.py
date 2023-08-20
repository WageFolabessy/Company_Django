from django.db import models
# Create your models here.

class Employee(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    company = models.ForeignKey("Company.Company", on_delete=models.CASCADE)
    
