from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import  CommentSerializers,PostSerializers
from Posts.models import PostLikes,Posts,PostComments
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from user.models import MyUser

# Create your views here.

#--------------- user post created and post delete update ----------------- #
class UserPosts(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    authentication_classes =  [JWTAuthentication]
    permission_classes = [IsAuthenticated]
     
    #-------- post created ------- #
    def create(self,request):
        try:
            copy =  request.data.copy()
            print(copy)
            copy.update({"user_id":request.user.id})
            print(copy)
            serializerss = PostSerializers(data = copy)
            if serializerss.is_valid():
                serializerss.save()
                return Response(serializerss.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializerss.errors,status = status.HTTP_400_BAD_REQUEST)
        except:
            messages = {"error":"client side error"}
            return Response(messages,status = status.HTTP_400_BAD_REQUEST)
            
# -------------- post like adding -------------------------------------- #
class PostLIke(APIView):
    authentication_classes =  [JWTAuthentication]
    permission_classes     =  [IsAuthenticated]

    def post(self, request):
        try:
            post_id = Posts.objects.get(id  = request.data.get('post_id') ) 
            user_id = MyUser.objects.get(id = request.user.id) 
            
            # condtions checking if post present or not in the database
            conditons = PostLikes.objects.filter(user_id=user_id, post_id=post_id).exists()
            if conditons:
                post_likes = PostLikes.objects.get(user_id = user_id)
                post_likes.delete()
                post = Posts.objects.get(id = request.data.get('post_id'))
                post.total_likes = post.total_likes - 1
                post.save()
                messages = {"success" : "Like removed","conditions" : False}
                return Response(messages,status=status.HTTP_204_NO_CONTENT)  
            else:
                post_likes = PostLikes()
                post_likes.user_id = user_id
                post_likes.post_id = post_id
                post_likes.save()
                post = Posts.objects.get(id = request.data.get('post_id'))
                post.total_likes = post.total_likes + 1
                post.save()
                messages = {"success" : "Like added","conditions" : True}
                return Response(messages,status = status.HTTP_201_CREATED)
        except:
            messages = {"error":"client side error"}
            return Response(messages,status = status.HTTP_400_BAD_REQUEST)
  
    
# -------------- post comment adding -------------------------------------- #
class comment(viewsets.ModelViewSet):
    queryset               =  PostComments.objects.all()
    serializer_class       =  CommentSerializers
    authentication_classes =  [JWTAuthentication]
    permission_classes     =  [IsAuthenticated]
    
    def create(self,request):
        try:
            post_id  = Posts.objects.get(id  = request.data.get('post_id'))  
            user_id  = MyUser.objects.get(id = request.user.id) 
            comments = request.data.get('comments')
            
            Postcomments = PostComments()
            Postcomments.post_id  = post_id
            Postcomments.user_id  = user_id
            Postcomments.comments = comments
            Postcomments.save()
            messages = {"success":"comment added"}
            return Response(messages,status = status.HTTP_201_CREATED)
        except:
            messages = {"error":"client side error"}
            return Response(messages,status = status.HTTP_400_BAD_REQUEST)
            
                 