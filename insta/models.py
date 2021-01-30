from django.db import models

class Post(models.Model):
    user_id = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
