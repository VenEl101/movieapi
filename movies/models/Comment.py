from django.db import models
from django.contrib.auth import get_user_model
from .Movie import Movie

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    