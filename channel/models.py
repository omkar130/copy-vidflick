from django.db import models
import taggit.managers
from taggit.managers import TaggableManager
from django.conf import settings
from core.models import user_directory_path

User = settings.AUTH_USER_MODEL


STATUS=(
    ("active","Active"),
    ("disabled","Disabled"),
)

class Channel(models.Model):

    channel_art = models.ImageField(upload_to=user_directory_path,null=True,blank=True) 
    image = models.ImageField(upload_to=user_directory_path,null=True,blank=True) 
    full_name = models.CharField(max_length=100) 
    channel_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    keywords = TaggableManager()
    joined = models.DateTimeField(auto_now_add=True) 
    status =  models.CharField(choices=STATUS,max_length=100,default='active')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True,related_name="channel_user")
    subscribers = models.ManyToManyField(User, related_name="user_sub")
    verified = models.BooleanField(default=False)
    feature = models.BooleanField(default=True)
    bussiness_email = models.CharField(max_length=500, null=True)
    bussiness_location = models.CharField(max_length=500, null=True)
    
    
    
    def __str__(self):
        return str(self.channel_name)