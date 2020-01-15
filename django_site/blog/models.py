from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    seo_title = models.CharField(null=True, blank=True, max_length=100)
    seo_description = models.CharField(null=True, blank=True, max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
