from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Image
from .serializers import ImageSerializer, UserSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ImageUploadView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class AllImagesView(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]  

    def get_queryset(self):
        return Image.objects.all().order_by('?')  

class UserImagesView(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]  

    def get_queryset(self):
        username = self.kwargs['username']  
        user = User.objects.get(username=username)  
        return Image.objects.filter(user=user)  