from django.urls import path
from cs import views

app_name = 'cs'

urlpatterns = [
    path('', views.HomeView.as_view(), name='main'),
]

