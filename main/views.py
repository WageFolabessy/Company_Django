from django.shortcuts import render
from Company.models import Company
from Employee.models import Employee
from Wallet.models import Wallet


def index(request):
    companies = Company.objects.all()
    employees = Employee.objects.all()
    wallets   = Wallet.objects.all()
    
    context = {
        'companies': companies,
        'employees': employees,
        'wallets'  : wallets,
    }
    return render(request, 'index.html', context)