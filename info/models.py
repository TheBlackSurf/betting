from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from core.models import Profile


class Info(models.Model):
    body = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    post = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return (f'{self.author} - {self.body}')
