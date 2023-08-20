from django.db import models
from django.utils import timezone
# Create your models here.

class Wallet(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.OneToOneField("Employee.Employee", on_delete=models.CASCADE)
    bank = models.CharField(max_length=50)
    amount = models.BigIntegerField()
    deleted_at = models.DateTimeField(default=timezone.now)
