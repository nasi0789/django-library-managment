from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=30)
#     Email = forms.EmailField()
#     Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))




class AdminSigupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1']
    def save(self, commit: bool = ...) -> Any:
        return super().save(commit)
    
            
class StudentUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1']
        
class AdminLogForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
    
class StdLogForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
    
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['enrollment','branch']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','category']
        
class IssuedBookForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    isbn2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Name and isbn", to_field_name="isbn",label='Name and Isbn')
    enrollment2=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Name and enrollment",to_field_name='enrollment',label='Name and enrollment')