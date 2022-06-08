from venv import create
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	body 		= 	models.TextField()
	created_on 	= 	models.DateTimeField(default=timezone.now)
	author 		= 	models.ForeignKey(User, on_delete=models.CASCADE)
	likes 		= 	models.ManyToManyField(User, blank=True, related_name='likes')
	dislikes 	= 	models.ManyToManyField(User, blank=True, related_name='dislikes')
	
	def __str__(self):
		return self.body


class Vote(models.Model):
	created 	= 	models.DateTimeField(auto_now_add=True, blank=True)
	name 		= 	models.CharField(max_length=200)
	author 		= 	models.ForeignKey(User, on_delete=models.CASCADE)
	post 		= 	models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)	







