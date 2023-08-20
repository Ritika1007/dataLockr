from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #retrieve subfolders
    path('', views.databag_view, name='databag'),
    #retrieve files in subfolder
    path('subfolder/<int:subfolder_id>/', views.subfolder_view, name='subfolder'),
    #retrieve files content
    path('file/<int:file_id>/', views.file_view, name='file'),
    #update files content
    path('file/<int:file_id>/update', views.edit_file, name='edit_file'),
    #delete files and subfolders
    path('subfolder/<int:subfolder_id>/delete/', views.delete_subfolder, name='delete_subfolder'),
    path('file/<int:file_id>/delete/', views.delete_file, name='delete_file'),
]
