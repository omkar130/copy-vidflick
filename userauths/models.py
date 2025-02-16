from django.db import models
from django.db.models.signals import post_save
from django.db.models import Model
from django.contrib.auth.models import AbstractUser
from core.models import Video


#AbstractUser is use to create custom user model

class User(AbstractUser):
    email = models.EmailField(unique=True,null=True)
    username = models.CharField(max_length=1000)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userauths_groups', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userauths_permissions',
        blank=True
    )
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return str(self.username)
    
    
class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    saved_videos = models.ManyToManyField(Video, null=True,blank=True)
    
    
    def __str__(self):
        return str(self.user)


def  create_user (sender,instance,created,**kwargs):       #kwargs - keyword argument when signal passed. instance-user instance, sender-user, created-boolean, it will be true if user is created.
    if created:
        Profile.objects.create(user=instance)
        
def save_user(sender,instance,**kwargs):
    instance.profile.save()                        # profile is attr of user instance
    
    
post_save.connect(create_user,sender=User)
post_save.connect(save_user,sender=User)
         