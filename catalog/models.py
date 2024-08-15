from django.db import models

from users.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование товара',
        help_text='Введите наименование товара'
    )
    title = models.TextField(
        max_length=150,
        verbose_name='Описание',
        help_text='Введите описание товара'
    )
    picture = models.ImageField(
        upload_to='products/photo',
        blank=True,
        null=True,
        verbose_name='Изображение',
        help_text='Загрузите изображение'
    )
    category = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Введите наименвание категории'
    )
    cost = models.IntegerField(
        verbose_name='Цена товара',
        help_text='Введите цену товара'
    )

    def __str__(self):
        return self.name, self.title, self.picture, self.category, self.cost

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Введите наименование категории'
    )
    title = models.TextField(
        max_length=150,
        verbose_name='Описание',
        help_text='Введите описание'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Автор',
        null=True,
        blank=True,
        related_name='users'
    )
    def __str__(self):
        return self.name, self.title

class Version(models.Model):
    product_version = models.ForeignKey(
        related_name='version',
        to='Product',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Продукт',
    )
    name_product = models.CharField(
        max_length=100,
        verbose_name='Наименование товара',
        help_text='Введите наименование товара'
    )
    number_version = models.IntegerField(
        verbose_name='Описание',
        help_text='Введите номер версии'
    )
    name_version = models.CharField(
            max_length=100,
            verbose_name='Наименование версии',
            help_text='Введите наименование версии'
    )
    version_indicator = models.BooleanField(
        verbose_name='Индикатор версии',
        help_text='Отметьте, если версия актуальна'
    )
    def __str__(self):
        return self.product_version, self.name_product, self.number_version, self.name_version, self.version_indicator

