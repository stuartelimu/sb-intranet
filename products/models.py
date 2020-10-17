from django.db import models
from cloudinary.models import CloudinaryField 
from tinymce import HTMLField
from django.conf import settings

class ProductType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(max_length=200)
    description = HTMLField()
    procedures = HTMLField(blank=True)
    product = models.ForeignKey('ProductType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Notification(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=200)
    answer = HTMLField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Tool(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name


class RecognitionBoard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    achievement = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Promo(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    banner = CloudinaryField('banner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Troubleshoot(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

