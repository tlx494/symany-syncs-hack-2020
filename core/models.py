from django.db import models

# Create your models here.

class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True)
    link = models.TextField(blank=False)
    