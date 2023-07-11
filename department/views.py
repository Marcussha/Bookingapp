from django.shortcuts import render, redirect
from department.models import Departments 
from department.forms import DepartmentForm

def create(request):
    if request.method=="POST":
        form=DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("index")
            except:
                pass
    else:
        form=DepartmentForm()
        return render(request, 'department/create.html',{'form': form})
    
def index (request):
    departments = Departments.objects.all()
    return render(request, 'department/index.html', {'departments':departments})

def edit(request, id):
    departments = Departments.objects.get(departmentid = id)
    return render(request, 'department/edit.html',{'departments':departments})

def update(request, id):
    departments = Departments.objects.get(departmentid = id)
    form = DepartmentForm(request.POST, instance = departments)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'department/edit.html', {'department':departments})

def clear(request, id):
    departments = Departments.objects.get(departmentid = id)
    departments.delete()
    return redirect('index')       

# Create your views here.
