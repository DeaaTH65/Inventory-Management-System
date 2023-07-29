from rest_framework.serializers import ModelSerializer
from app_inventory.models import Product, Purchase
from app_users.models import Profile


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