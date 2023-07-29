from rest_framework.serializers import ModelSerializer
from app_inventory.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'