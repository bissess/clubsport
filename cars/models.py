from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Бренд')
    slug = models.SlugField(max_length=250, verbose_name='Слаг Бренда', unique=True)

    def get_absolute_url(self):
        return reverse('cars:brands', kwargs={'brand_slug': self.slug})

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Модель автомобиля')
    slug = models.SlugField(max_length=250, verbose_name='Слаг модели', unique=True)
    image = models.ImageField(upload_to='cars_catalog', verbose_name='Изображение автомобиля', default=None, null=True,
                              blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('cars:models', kwargs={'model_slug': self.slug})

    def __str__(self):
        return f'{self.brand.name} | {self.name}'