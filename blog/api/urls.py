from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blogs/', views.blog_list, name = "blog_list"),
    path('blogs/<int:blog_id>', views.blog_detail, name = "blog_detail"),
    
    path('text/', views.text_list, name = "text_list"),
    path('texts/<int:text_id>', views.text_detail, name = "text_detail"),
    
]
