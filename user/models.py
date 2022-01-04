from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.




class MyUser(AbstractUser):
    mobile_number =  models.CharField(max_length=10, unique=True)
    birth_date    =  models.DateField(null=True, blank=True)
    profile_pic   =  models.ImageField(upload_to='profile_pics', null = True, blank = True,)
    bio           =  models.TextField(blank=True ,null=True)
    is_private    =  models.BooleanField(default=False)
    followers   = ArrayField(models.IntegerField(null= True),null=True)
    followings   = ArrayField(models.IntegerField(null= True),null=True)
    
    @property
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
