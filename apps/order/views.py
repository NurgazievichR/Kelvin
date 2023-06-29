from rest_framework import viewsets

from apps.order.models import Order 
from apps.order.serializres import OrderSerializer

class OrderApiViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    