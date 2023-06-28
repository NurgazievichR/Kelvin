from rest_framework.viewsets import ModelViewSet

from apps.promocode.models import Promocode
from apps.promocode.serializers import PromocodeSerializer

class PromocodeViewSet(ModelViewSet):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer
 
