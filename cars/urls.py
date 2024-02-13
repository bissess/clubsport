from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('cars/', views.CarsCatalogView.as_view(), name='main'),
    path('brands/<slug:brand_slug>/', views.CarsView.as_view(), name='brands'),
    path('brands/model/<slug:model_slug>/', views.CarsDetailView.as_view(), name='models')
]