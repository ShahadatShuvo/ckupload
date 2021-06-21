from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = RichTextField()
    content_upload = RichTextUploadingField()

    def __str__(self):
        return self.title
