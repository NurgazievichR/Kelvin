from django.db import models

class Setting(models.Model):
    title = models.CharField('Название',max_length=365,blank=True, null=True )
    icon = models.ImageField('Иконка',blank=True, null=True, upload_to='media/images/')
    aboutus = models.CharField('О нас', max_length=365,blank=True, null=True)
    description = models.CharField('Описание', max_length=365,blank=True, null=True)
    address = models.CharField('Адрес',max_length=100,blank=True, null=True)
    phone = models.CharField('Телефон', max_length=15,blank=True, null=True)
    email = models.CharField(max_length=50,blank=True, null=True)
    facebook = models.CharField(blank=True,max_length=50, null=True)
    instagram = models.CharField(blank=True,max_length=50, null=True)
    twitter = models.CharField(blank=True,max_length=50, null=True)
    youtube = models.CharField(blank=True, max_length=50, null=True)
    create_at=models.DateTimeField('Создано',auto_now_add=True)
    update_at=models.DateTimeField('Изменено',auto_now=True)

    def __str__(self):
        return f'{self.title}'

    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
