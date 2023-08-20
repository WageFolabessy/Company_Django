from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
# Create your views here.

def index(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'Employee/index.html', context)

def create_or_store(request):
    return render(request, 'Employee/add.html')


def detail(request, id):
    return render(request, 'Employee/detail.html')

def edit_or_update(request, id):
    return render(request, 'Employee/update.html')


def delete(request, id):
    pass