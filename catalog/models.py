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

class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
        help_text='Введите заголовок блога'
    )
    slug = models.CharField(
        max_length=100,
        verbose_name='Ссылка',
        help_text='Сгенерируется автоматически из заголовка'
    )
    content = models.TextField(
        verbose_name='Содержание',
        help_text='Введите текст блога'
    )
    preview_picture = models.ImageField(
        upload_to='blog/photo',
        blank=True,
        null=True,
        verbose_name='Превью изображение',
        help_text='Загрузите превью изображение'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Создано автоматически'
    )
    published_sign = models.BooleanField(
        default=False,
        verbose_name='Опубликовано',
        help_text='Отметьте, если блог опубликован'
    )
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество просмотров',
        help_text='Счетчик просмотров'
    )

    def __str__(self):
        return self.title, self.slug, self.preview_picture, self.date_created, self.published_sign, self.views_counter