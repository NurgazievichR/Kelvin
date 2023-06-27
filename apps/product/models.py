from django.db import models

class Product(models.Model):

    SIZES = [
        '52 / XL',
        '44 / XS',
        '46 / S',
        '48 / M',
        '50 / L',
    ]

    title = models.CharField('Название', max_length=365)
    main_image = models.ImageField('Фото', upload_to='media/cloth_photos/')
    description = models.CharField('Описание', max_length=365)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=10)
    size = models.CharField('Размер', max_length=15, choices=[(size, size) for size in SIZES])

