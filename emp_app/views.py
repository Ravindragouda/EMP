from django.shortcuts import render

from emp_app.models import Employee

# Create your views here.
def index(request):
    emps=Employee.objects.all()
    return render(request,"index.html", {'emps':emps})


def submit(request):
    return render(request,"create_employee.html")   