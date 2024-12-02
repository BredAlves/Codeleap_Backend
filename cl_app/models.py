from django.db import models
from django.utils import timezone

class Post(models.Model):
    username = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_ip = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return self.title