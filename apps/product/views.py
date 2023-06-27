from rest_framework.viewsets import ModelViewSet

from apps.product.models import Product, ProductImage
from apps.product.serializers import ProductSerializer, ProductImageSerializer


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageAPIViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer