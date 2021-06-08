from django.db import models


class DiaryPost(models.Model):
    timestamp = models.DateField()
    post = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return None
