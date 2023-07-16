from django.db import models

class Product(models.Model):
    title = models.CharField('Название', max_length=365)
    description = models.CharField('Описание', max_length=365)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=10)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title}----{self.id}"
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/cloth_photos/')

    def __str__(self):
       return f"IMAGE: {self.product.title}-------{self.id}"
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class ProductSize(models.Model):
    product = models.ForeignKey(Product, related_name='product_sizes', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=365)

    def __str__(self):
        return f"{self.product.title}---------{self.id}"
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'