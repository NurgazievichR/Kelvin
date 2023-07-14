from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from apps.order.models import Order, Address
from apps.order.serializres import OrderSerializer, AddressSerializer

class OrderApiViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class AddressApiViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['region', 'city']

