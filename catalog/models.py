from django.db import models

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


    def __str__(self):
        return self.name, self.title

