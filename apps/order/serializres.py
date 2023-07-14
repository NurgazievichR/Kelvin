from rest_framework import serializers 
from rest_framework.validators import ValidationError
from decimal import Decimal

from apps.order.models import Order, OrderItem, Address
from apps.product.models import Product
from apps.promocode.models import Promocode

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['region', 'city']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['name', 'surname', 'email', 'phone_number', 'address', 'promocode', 'order_items', 'total_price']

    def create(self, validated_data):   
        promocode = validated_data.get('promocode')
        promocode_model = Promocode.objects.filter(code=promocode)
        promocode_list = list(Promocode.objects.filter(is_active=True).values_list('code', flat=True))
        total_price = Decimal(0)

        if promocode not in promocode_list and promocode != "":
            raise ValidationError('Такого промокода нет!')

        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)  

        for order_item_data in order_items_data:
            product_ = order_item_data['product']
            quantity = order_item_data['quantity']
            total_price += product_.price * quantity
            product = Product.objects.get(pk=product_.id)
            OrderItem.objects.create(order=order, quantity=quantity, product=product)

        if promocode in promocode_list:
            total_price = total_price/100*promocode_model[0].discount

        order.total_price = total_price
        return order
    
