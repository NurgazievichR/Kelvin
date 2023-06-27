from rest_framework import serializers

from apps.product.models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'

