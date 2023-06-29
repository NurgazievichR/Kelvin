from rest_framework import serializers 

from apps.order.models import Order, OrderItem
from apps.product.models import Product
from apps.promocode.models import Promocode

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['name', 'surname', 'email', 'phone_number', 'address', 'promocode', 'order_items']

    def create(self, validated_data):   
        promocode = validated_data.get('promocode')
        promocode_list = list(Promocode.objects.filter(is_active=True).values_list('code', flat=True))

        if promocode != "" and promocode in promocode_list:
            print('hey')


        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)  


        for order_item_data in order_items_data:
            product_ = order_item_data['product']
            quantity = order_item_data['quantity']
            product = Product.objects.get(pk=product_.id)
            OrderItem.objects.create(order=order, quantity=quantity, product=product)

        return order
    
