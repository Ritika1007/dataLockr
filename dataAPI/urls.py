from django.urls import path
from .views import *

urlpatterns = [
    path('subfolders/', SubfolderListCreateAPIView.as_view(), name='subfolder-list-create'),
    path('subfolders/<str:pk>', SubfolderListCreateAPIView.as_view(), name='subfolder-delete'),
]