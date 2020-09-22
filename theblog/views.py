from django.shortcuts import render

from .models import *
from .forms import *

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin
# Create your views here.


# def home(request):
#     return render(request, 'theblog/index.html',{})

class CommonData(ContextMixin):
    def get_context_data(self,*args,**kwargs):
        cat_menu =Category.objects.all()
        context = super(CommonData,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class HomeView(ListView, CommonData):
    model = Post
    template_name = "theblog/index.html"
    context_object_name = 'blogs'
    # ordering = ['-id']
    ordering = ['-date']


class PostView(DetailView, CommonData):
    model = Post
    template_name = 'theblog/post.html'
    context_object_name = 'post'

class CreatePostView(CreateView, CommonData):
    model = Post
    form_class = PostForm
    template_name = 'theblog/addpost.html'
    # fields = '__all__'
    # fields = ('title', 'author','body')
    
class UpdatePostView(UpdateView, CommonData):
    model = Post
    form_class = UpdatePostForm
    template_name = 'theblog/editpost.html'
    
class DeletePostView(DeleteView, CommonData):
    model = Post
    template_name = 'theblog/deletepost.html'
    success_url = reverse_lazy('home')
    
class AddCategoryView(CreateView, CommonData):
    model = Category
    template_name ='theblog/addcategory.html'
    form_class = AddCategoryForm
    success_url =reverse_lazy('home')
    
# def CategotyPostView(request, cats):
#     category_post = Post.objects.filter(category=cats)
#     return render(request, 'theblog/categories.html',{'cats':category_post, 'title_name':cats})

class CategoryPostView(ListView, CommonData):
    model = Post
    template_name = "theblog/categories.html"
    
    def get_object(self):
        self.cat_name = self.kwargs['cats']
        return self.cat_name
    
    def get_context_data(self,*args, **kwargs):
        category_post = Post.objects.filter(category=self.get_object())
        context = super(CategoryPostView, self).get_context_data(*args, **kwargs)
        context["cats"] = category_post
        context["title_name"] = self.get_object()
        return context