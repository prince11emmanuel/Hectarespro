from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    video = models.FileField(upload_to='blog-video',blank=True, null=True)
    content = models.TextField()
    markas_soled = models.BooleanField(default=False)
    markas_available=models.BooleanField(default=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now)



    location_name = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)


    def __str__(self):
        return self.title
    
    def get_map_url(self):
        if self.latitude and self.longitude:
            return f"https://www.google.com/maps/search/?api=1&query={self.latitude},{self.longitude}"
        return None
    
    def has_location(self):
        return self.latitude is not None and self.longitude is not None