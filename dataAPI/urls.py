from django.urls import path
from .views import *

urlpatterns = [
    path('subfolders/', SubfolderAPIView.as_view(), name='subfolder-list-create'),
    path('subfolders/<int:pk>', SubfolderAPIView.as_view(), name='subfolder-delete'),
    path('subfolders/<int:subfolder_id>/files', JSONFileAPIView.as_view(), name='file-list-create'),
    path('subfolders/<int:subfolder_id>/file/<int:file_id>', JSONFileAPIView.as_view(), name='file-detail'),
]