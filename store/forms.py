from django.forms import ModelForm
from .models import *

class FileForm(ModelForm):
    class Meta:
        model = FileData
        fields = '__all__'