from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(null=True, blank=True, upload_to='profiles/')
    profile_bio = models.CharField(null=True, blank=True, max_length=200)
    facebook_link = models.CharField(null=True, blank=True, max_length=200)
    date_modified = models.DateTimeField(User, auto_now=True)
    
    def __str__(self):
        return self.user.username

 