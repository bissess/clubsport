# Generated by Django 4.2.6 on 2024-02-06 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг категории')),
            ],
        ),
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок поста')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг поста')),
                ('description', models.TextField(verbose_name='Содержание поста')),
                ('image', models.ImageField(blank=True, default=None, upload_to='post_images', verbose_name='Изображение поста')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='news.newscategory')),
            ],
        ),
    ]
