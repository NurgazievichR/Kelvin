from django.db import models

class Promocode(models.Model):
    code = models.CharField('Промокод',max_length=30, unique=True)
    discount = models.DecimalField('Скидка', max_digits=5, decimal_places=2)
    is_active = models.BooleanField('Активно', default=True)

    def __str__(self):
        return f'{self.code}'

    class Meta:
        ordering = ('-id')
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'
