from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny        
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User    
from .models import Profile                   

class ProfileView(viewsets.ModelViewSet):      
  serializer_class = ProfileSerializer        
  queryset = Profile.objects.all()    

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
