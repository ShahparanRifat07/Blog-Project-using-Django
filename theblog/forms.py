from django import forms
from .models import *

choices = Category.objects.all().values_list('name','name')
choice_list = []
for i in choices:
    choice_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','body')
    
        widgets = {
            'title' : forms.TextInput(attrs ={'class': 'form-control', 'placeholder':'Write the title here'}),
            'author' : forms.Select(attrs ={'class': 'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs ={'class': 'form-control'}),
            'body' : forms.Textarea(attrs ={'class': 'form-control', 'placeholder':'Write down the body'}),
            
        }
        
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice_list,attrs ={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }
        
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Write the Category Name'})
        }