from dataclasses import field
from pyexpat import model
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User,UserChannel,UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    
    class Meta:
        model = UserProfile
        fields="__all__"
        
class UserSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields='__all__'