from django.contrib.postgres import fields
from user.models import MyUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator



class UserReg_Serialzer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=MyUser.objects.all(),message=("Email already exists"))])
                                        
    class Meta:
        model = MyUser
        fields =['id', 'username', 'password','mobile_number','first_name','email']
        
        extra_kwargs = {'password':{
        'write_only':True,
        'required' : True
        }}
        
    def create(self,validated_data):
        user = MyUser.objects.create_user(**validated_data)
        # Token.objects.create(user = user)
        return user
    

class LoginSerializer(serializers.ModelSerializer):
     class Meta: 
        model = MyUser
        fields =['username', 'password']
        
        extra_kwargs = {'password':{
        'write_only':True,
        'required' : True
        }}
        
class UserCostomize(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id','username','email','first_name','profile_pic','mobile_number','password']
        
        extra_kwargs = {'password':{
        'write_only':True,
        'required' : True
        }}
        
        
class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = MyUser
        fields = ['id','profile_pic']
        
    
        
        
    
  
    
    
    
        
   
        
