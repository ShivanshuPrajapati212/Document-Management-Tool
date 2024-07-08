from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title