from django.urls import path
from . import views

urlpatterns = [
    path('', views.uploadFile, name='upload_file'),
    path('list/', views.fileList, name='file_list'),
    path('file/<int:pk>', views.deleteFile, name='file'),
    path("list_file/", views.ListFileAPIView.as_view()),
    path("create/", views.CreateFileAPIView.as_view()),
    path("update/<int:pk>/", views.UpdateFileAPIView.as_view()),
    path("delete/<int:pk>/", views.DeleteFileAPIView.as_view()),

]