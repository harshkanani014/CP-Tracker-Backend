from django.db import models

# Create your models here.
class postcard(models.Model):
    heading = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    alt = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)

