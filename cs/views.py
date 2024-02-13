from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from news.models import NewsPost


class HomeView(ListView):
    template_name = 'cs/index.html'
    context_object_name = 'cars_images'
    paginate_by = 1

    def get_queryset(self):
        static_images = [
            '/static/cs/images/car-2.jpg',
            '/static/cs/images/car-1.jpg',
            '/static/cs/images/car-3.jpg',
        ]
        return static_images

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = NewsPost.objects.all()
        return context


