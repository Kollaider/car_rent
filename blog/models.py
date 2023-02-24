from django.contrib.auth.models import User
from django.db import models



class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True)
    categories = models.ManyToManyField('Category')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment model"""
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text[:20] +  '...'


class Category(models.Model):
    """Category model"""
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Category model"""
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title