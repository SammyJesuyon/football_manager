from rest_framework import serializers
from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        
    # Prevents the password from showing after submission
    extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        new_user.set_password(validated_data["password"])
        new_user.save()
        return new_user
       
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField()