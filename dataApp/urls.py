from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #retrieve subfolders
    path('', views.databag_view, name='databag'),
    #retrieve files in subfolder
    path('subfolder/<str:subfolder_id>/', views.subfolder_view, name='subfolder'),
    #retrieve files content
    path('file/<int:file_id>/', views.file_view, name='file'),
]
