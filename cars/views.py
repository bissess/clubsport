from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from .models import Brand, CarModel


class CarsCatalogView(ListView):
    template_name = 'cars/index.html'
    context_object_name = 'brands'

    def get_queryset(self):
        brands = Brand.objects.all()
        return brands

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['models'] = CarModel.objects.all()
        context['brands'] = Brand.objects.all()
        return context


class CarsView(ListView):
    template_name = 'cars/index.html'
    context_object_name = 'models'

    def get_queryset(self):
        return CarModel.objects.filter(brand__slug=self.kwargs['brand_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context


class CarsDetailView(DetailView):
    template_name = 'cars/index.html'
    context_object_name = 'model_image'
    slug_url_kwarg = 'model_slug'

    def get_queryset(self):
        return CarModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_model = context['object']
        context['models'] = CarModel.objects.filter(brand=selected_model.brand)
        context['brands'] = Brand.objects.all()
        return context
