from django.db import models
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    field = models.CharField(max_length=100)
    
    def total_employee(self):
        return self.employee_set.count()

