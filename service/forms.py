from django import forms  
from service.models import Services 

class ServiceForm(forms.ModelForm):  
    class Meta:  
        model = Services
        fields = [ 'serviceid','name_service'] 
        widgets = { 'serviceid': forms.TextInput(attrs={ 'class': 'form-control' }), 
                    'name_service': forms.TextInput(attrs={ 'class': 'form-control' }),     
        }