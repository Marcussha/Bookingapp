from django.shortcuts import render, redirect
from service.models import Services
from service.forms import ServiceForm


def create(request):
    if request.method=='POST':
        form=ServiceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("index")
            except:
                 pass
    else:
        form = ServiceForm()
    return render(request,'service/create.html',{'form' :form})

def show(request):
    services = Services.objects.all()
    return render(request,'service/index.html',{'services' :services})
             
def edit(request, id):
    service = Services.objects.get(serviceid=id)
    return render(request,'service/edit.html',{'service' :service}) 

def update(request, id):
    service = Services.objects.get(serviceid=id)
    form = ServiceForm(request.POST, instance = service)
    if form.is_valid():
        form.save()
        return redirect("index")
    
    return render(request,'service/edit.html',{'service': service}) 
    

def clear(request, id):
    services = Services.objects.get(serviceid =id)
    services.delete()
    return redirect('index')            

