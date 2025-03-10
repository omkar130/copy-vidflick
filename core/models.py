from django.db import models
import taggit.managers
from taggit.managers import TaggableManager
from django.conf import settings


User = settings.AUTH_USER_MODEL

#This is Tuple(datatype in python) (key,value) collection of items.
VISIBILITY=(
    ("member_only","Member Only"),
    ("unlisted","Unlisted"),
    ("private","Private"),
    ("public","Public")
)

def user_directory_path(instance,filename):
    return "user_{0}{1}".format(instance.user.id,filename)  #instance.user.id: This will get the id of the user related to the UserProfile instance.


#models.Model is base class which provide us methods to interact with database
class Video(models.Model):
    video = models.FileField(upload_to=user_directory_path)  # getting video from user and storing with user id by calling user_directory_path function.
    image = models.ImageField(upload_to=user_directory_path,null=True,blank=True) 
    title = models.CharField(max_length=100) 
    description = models.TextField(null=True, blank=True)
    tags = TaggableManager()
    date = models.DateTimeField(auto_now_add=True) # auto_now_add means it will take time and date of uploading the video.
    visibility =  models.CharField(choices=VISIBILITY,max_length=100,default='public')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name="user") # on_delete to specify if user get's delet then video should also get delete or not. CASCADE (delete)and SET_NULL(keep)
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User,related_name="likes")
    dislikes = models.ManyToManyField(User,related_name="dislikes")
    
    def __str__(self):
        return str(self.title)
    
    
class Comment(models.Model):
    comment = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name="comment_user")    
    active = models.BooleanField(default=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return str(self.comment)
    
    
    