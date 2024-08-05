from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    description = models.TextField()
    file = models.FileField(upload_to='blog_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
