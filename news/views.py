from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from news.models import NewsCategory, NewsPost


class NewsHomeView(ListView):
    template_name = 'news/index.html'
    context_object_name = 'categories_list'

    def get_queryset(self):
        category = NewsCategory.objects.all()
        return category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = NewsPost.objects.all()
        return context


class NewsPostsView(ListView):
    template_name = 'news/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return NewsPost.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = NewsCategory.objects.all()
        return context


class DetailNewsView(DetailView):
    template_name = 'news/detail_news.html'
    context_object_name = 'post'

    def get_queryset(self):
        return NewsPost.objects.all()