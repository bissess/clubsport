from django.db import models
from django.urls import reverse


class NewsCategory(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Наименование категории')

    slug = models.SlugField(max_length=255,
                            verbose_name='Слаг категории',
                            unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news:news_by_category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория Новости'
        verbose_name_plural = 'Категории Новостей'


class NewsPost(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Заголовок поста',
                             blank=False)

    slug = models.SlugField(max_length=255,
                            verbose_name='Слаг поста',
                            unique=True)

    description = models.TextField(verbose_name='Содержание поста')

    image = models.ImageField(upload_to='post_images',
                              verbose_name='Изображение поста',
                              default=None,
                              blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(NewsCategory,
                                 on_delete=models.CASCADE,
                                 related_name='post')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail_news', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория Поста'
        verbose_name_plural = 'Категории Постов'
