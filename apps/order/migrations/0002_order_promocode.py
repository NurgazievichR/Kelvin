# Generated by Django 4.2.2 on 2023-06-29 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='promocode',
            field=models.CharField(blank=True, max_length=365, null=True, verbose_name='Промокод'),
        ),
    ]
