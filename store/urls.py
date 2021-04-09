from django.urls import path
from . import views

urlpatterns = [
    path('', views.uploadFile, name='upload_file'),
    path('list/', views.fileList, name='file_list'),
    path('file/<int:pk>', views.deleteFile, name='file'),
]