from django.db import models

# Create your models here.


class postcard(models.Model):
    id = models.IntegerField(primary_key=True)
    heading = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    alt = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    link = models.CharField(max_length=100),
    created_at = models.DateTimeField(auto_now_add=True)


class subscribers(models.Model):
    email = models.EmailField(max_length=100)
