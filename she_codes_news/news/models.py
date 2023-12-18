from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=255, default='uncategorized')
    content = models.TextField()
    preview = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
