from multiprocessing import Value
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
    
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
    
class TransferSerializer(serializers.Serializer):
    player = serializers.ChoiceField(choices=Player.objects.all())
    player_value = serializers.DecimalField(max_digits=20, decimal_places=2, 
                                        default = Player.objects.all().values)
    transferred_from = serializers.CharField(default=Team.objects.all())
    transferred_to = serializers.ChoiceField(choices=Team.objects.all())
    
    