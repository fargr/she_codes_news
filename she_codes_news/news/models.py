from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
