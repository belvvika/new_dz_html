from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    title = models.TextField(max_length=150, verbose_name='Описание')
    picture = models.ImageField(verbose_name='Изображение')
    category = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Категория')
    cost = models.IntegerField(verbose_name='Цена за штуку')
    date_of_create = models.DateField(verbose_name='Дата создания')
    last_modified_date = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name, self.title, self.picture, self.picture, self.category, self.cost, self.date_of_create, self.last_modified_date

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    title = models.TextField(max_length=150, verbose_name='Описание')


    def __str__(self):
        return self.name, self.title