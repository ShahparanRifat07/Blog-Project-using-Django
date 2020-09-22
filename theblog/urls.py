from django.urls import path

from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('post/<int:pk>/',PostView.as_view(),name='post_url'),
    path('addblog/',CreatePostView.as_view(),name='addpost_url'),
    path('post/editpost/<int:pk>',UpdatePostView.as_view(),name='update_url'),
    path('post/deletepost/<int:pk>',DeletePostView.as_view(),name='delete_url'),
    path('add_category/',AddCategoryView.as_view(),name='category_url'),
    path('category/<str:cats>/',CategoryPostView.as_view(),name='category_post_url')
]
