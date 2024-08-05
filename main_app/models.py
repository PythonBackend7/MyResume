from django.db import models
from django.contrib.auth.models import User


class About(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_images/')
    description = models.TextField()


class Experience(models.Model):
    image = models.ImageField(upload_to='experience_images/')
    work_place = models.CharField(max_length=200)
    start_finish_year = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)


class Work(models.Model):
    image = models.ImageField(upload_to='work_images/')
    link = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


class Service(models.Model):
    image = models.ImageField(upload_to='service_images/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()