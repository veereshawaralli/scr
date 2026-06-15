from django import forms
from .models import student,course

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields=['first_name','last_name','email','courses']
        widgets={
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'courses': forms.SelectMultiple(attrs={'class': 'form-select', 'data-toggle': 'dropdown'}), 
        }

class CourseForm(forms.ModelForm):  
    class Meta:  
        model = course  
        fields = ['name', 'discription']  
        widgets = {  'name': forms.TextInput(attrs={'class': 'form-control'}),  
                   'discription': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  
                } 