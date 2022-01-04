from django.db import models
from user.models import MyUser
from django.utils import timezone

# Create your models here.

class Posts(models.Model):
    description = models.TextField(max_length=250,null=True)
    image1 = models.ImageField(upload_to='posts')
    total_likes = models.IntegerField(default= 0)
    comments = models.TextField(max_length=250,null=True)
    location = models.TextField(max_length=250,null=True)
    user_id = models.ForeignKey(MyUser,on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)
    

class PostLikes(models.Model):
    user_id = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    like = models.IntegerField(default=1)
    
    
class PostComments(models.Model):
    comments = models.TextField(max_length=250,null=True)
    user_id = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)
    
    
    
