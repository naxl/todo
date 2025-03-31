from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.ImageField(upload_to = "images", default = None)
    