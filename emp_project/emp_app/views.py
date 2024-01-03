
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from .models import Role
from .models import Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def view_employee(request):
    emp = Employee.objects.all()
    context = {
          'emp':emp
    }
    print(context)
    return render(request, 'view_employee.html', context)

def add_employee(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       dept = int(request.POST['dept'])
       salary = int(request.POST['salary'])
       bonus = int(request.POST['bonus'])
       role = int(request.POST['role'])
       phone = int(request.POST['phone'])
       emp_new = Employee(first_name=first_name, last_name=last_name, dept_id=dept,
                      salary=salary, bonus=bonus, role_id=role, phone=phone, hire_date=datetime.today())
       emp_new.save()
       return HttpResponse('Added Employee Successfully')
    elif request.method=='GET':
         return render(request, 'add_employee.html')
    else:
        return HttpResponse("An Exception Occured")


def delete_employee(request,emp_id = 0):
    if emp_id:
        try:
            emp_removed = Employee.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse("Employee Removes Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emp = Employee.objects.all()
    context = {
        'emp':emp
    }

    return render(request, 'delete_employee.html',context)

def update_employee(request):
    if request.method == 'POST':
       name = request.POST['name']
       dept = request.POST['dept']
       role = request.POST['role']
       emp = Employee.objects.all()
       if name:
           emp = emp.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
       if dept:
           emp = emp.filter(dept__name=dept)
       if role:
           emp = emp.filter(role__name = role)

       context = {
            'emp':emp
       }
       return render(request, 'view_employee.html', context)

    elif request.method == 'GET':
        return render(request, 'update_employee.html')
    else:
        return HttpResponse('An Exception Occurred')


