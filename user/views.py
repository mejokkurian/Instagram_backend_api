from .serializers import UserReg_Serialzer,LoginSerializer,UserCostomize,FileSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from user.models import MyUser


# user creation view 
class UserRegistration(generics.GenericAPIView,mixins.CreateModelMixin):
    queryset = MyUser.objects.all()
    serializer_class = UserReg_Serialzer
    
    def post(self, request):
        return self.create(request)
    
 
#------------- user login view ----------------- #    
class UserLogin(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            
            user = authenticate(username=username, password=password)
            serializers = LoginSerializer(user)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    refresh = RefreshToken.for_user(user)
                    
                    return Response({
                        "user"  : serializers.data,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    })
                else:
                    message = {"error":"user is not activate"}
                    return Response(message,status=status.HTTP_404_NOT_FOUND)
            else:
                message = {"error" : "invalide password or username"}
                return Response(message,status=status.HTTP_404_NOT_FOUND)
        except:
            message = {"error" : "clients side error"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
            
                
# ------------- user edit,delete,update ---------- #
class Users(viewsets.GenericViewSet,mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin):
    authentication_classes =  [JWTAuthentication]
    permission_classes     =  [IsAuthenticated]
    queryset               =  MyUser.objects.all()
    serializer_class = UserCostomize
    


# -------------- user profile upload --------------- #
class profileupload(APIView):
    parser_classes          = (MultiPartParser, FormParser)
    authentication_classes  = [JWTAuthentication]
    permission_classes      = [IsAuthenticated]

    def post(self, request, format = None):
        try:
            file_serializer = FileSerializer(data=request.data)
            if file_serializer.is_valid():
                user  = MyUser.objects.get(id = request.user.id)
                user.profile_pic = request.FILES['profile_pic']
                user.save()
                message = {"success" : "profile pic created"}
                return Response(message, status=status.HTTP_201_CREATED)
            else:
                message = {"error" : "profile pic not created"}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        except:
            message = {"error" : "client side erroe"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
            


    

    




