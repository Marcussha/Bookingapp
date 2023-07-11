from django import forms
from department.models import Departments

class DepartmentForm(forms.ModelForm):
    class Meta:  
        model = Departments
        fields = [ 'departmentid','named'] 
        widgets = { 'departmentid': forms.TextInput(attrs={ 'class': 'form-control' }), 
                    'named': forms.TextInput(attrs={ 'class': 'form-control' }), 
    
    }