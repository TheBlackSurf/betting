from django.db import models

# Create your models here.

class Info(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']