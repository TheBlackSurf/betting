from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Vote(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def update(self, *args, **kwargs):
        kwargs.update({"updated": timezone.now})
        super().update(*args, **kwargs)

        return self

    def __str__(self):
        return self.name

# class User(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE)
#     vote = models.ForeignKey(Vote, on_delete=CASCADE)
    