from django.db import models

class FileData(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=True, null=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

