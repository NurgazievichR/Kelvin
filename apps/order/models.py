from django.db import models
from django.core.validators import validate_email
from apps.product.models import Product

class Order(models.Model):
    name = models.CharField('Имя', max_length=365)
    surname = models.CharField('Фамилия', max_length=365)
    email  = models.EmailField(validators=[validate_email])
    phone_number = models.CharField('Номер телефона', max_length=365)
    address = models.CharField('Адрес', max_length=365)

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name = 'Заказы'
        ordering = ('-id',)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'
    
    
