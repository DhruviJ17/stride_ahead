from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, UpdateAPIView,CreateAPIView,DestroyAPIView

def fileList(request):
    files = FileData.objects.all()
    return render(request, 'store/list.html', {'files': files})


def uploadFile(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'store/upload.html', {'form': form})


def deleteFile(request, pk):
    if request.method == 'POST':
        file = FileData.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')

class ListFileAPIView(ListAPIView):
    queryset = FileData.objects.all()
    serializer_class = FileSerializer

class CreateFileAPIView(CreateAPIView):
    queryset = FileData.objects.all()
    serializer_class = FileSerializer

class UpdateFileAPIView(UpdateAPIView):
    queryset = FileData.objects.all()
    serializer_class = FileSerializer

class DeleteFileAPIView(DestroyAPIView):
    queryset = FileData.objects.all()
    serializer_class = FileSerializer
