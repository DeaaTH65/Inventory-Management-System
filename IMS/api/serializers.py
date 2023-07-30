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