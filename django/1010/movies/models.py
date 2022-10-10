from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=20)
    movie_name = models.CharField(max_length=20)
    grade = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
