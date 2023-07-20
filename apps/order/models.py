from django.db import models
from django.core.validators import validate_email
from apps.product.models import Product

class Order(models.Model):
    name = models.CharField('Имя', max_length=365)
    surname = models.CharField('Фамилия', max_length=365)
    email  = models.EmailField(validators=[validate_email])
    phone_number = models.CharField('Номер телефона', max_length=365)
    address = models.CharField('Адрес', max_length=365)
    promocode = models.CharField('Промокод', max_length=365, blank=True, null=True)

    def __str__(self):
        return f'{self.id}--Имя:-{self.name}--Фамилия:-{self.surname}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-id',)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'
    
    
class Address(models.Model):
    region = models.CharField('Регион', max_length=365)
    city = models.CharField('Город', max_length=365)

    def __str__(self):
        return f'{self.region}////{self.city}'
    
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
    

class Street(models.Model):
    name = models.CharField('Улица', max_length=365)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'