from django.db import models

# Create your models here.

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