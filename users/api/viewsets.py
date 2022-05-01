from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 

from users import models
from users.api import serializers


class UserViewSet(ModelViewSet):
    queryset = models.CustomUser.objects.all() 
    serializer_class = serializers.UserSerializer
    
    # authentication
    #permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly ] 
