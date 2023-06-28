from rest_framework import serializers
from apps.promocode.models import Promocode

class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = '__all__'
        