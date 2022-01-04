from django.contrib.postgres import fields
from Posts.models import PostLikes, Posts,PostComments
from rest_framework import serializers
from user import models

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','description','image1','total_likes','comments','location','user_id']
        

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ['id','comments','user_id','post_id']
        
        

        
