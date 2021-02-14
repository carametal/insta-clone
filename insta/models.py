from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200)
