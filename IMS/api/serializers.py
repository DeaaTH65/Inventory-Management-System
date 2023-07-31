from rest_framework.serializers import ModelSerializer
from app_inventory.models import Product, Purchase
from app_users.models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
        
class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
        
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    
class UserRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    
class BuySerializer(ModelSerializer):
    class Meta:
        model = Purchase
        exclude = ['user', 'total_amount']