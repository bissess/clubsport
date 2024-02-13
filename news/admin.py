from django.contrib import admin

from news.models import NewsPost, NewsCategory

admin.site.register(NewsPost)

admin.site.register(NewsCategory)