from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def employeeList(request):
    context = Employee.objects.all()
    return render (request, "employee_register/list.html", {'context':context})

def employeeForm(request, id=0):
    if request.method == "GET":
        if id == 0 :
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        return render (request, "employee_register/form.html", {'form': form })

    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
                
        if form.is_valid():
            form.save()
        return redirect('/employee/list')    
        
        



def employeeDelete(request, id=0):
    employee = Employee.objects.get(pk=id)
    employee.delete()

    return render (request, "employee_register/list.html")
   
