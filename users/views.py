from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAdminUser

class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAdminUser]