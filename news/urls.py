from django.urls import path, include

from news import views

app_name = 'news'

urlpatterns = [
    path('news/', views.NewsHomeView.as_view(), name='news'),
    path('news/<slug:slug>/', views.NewsPostsView.as_view(), name='news_by_category'),
    path('news/detail/<slug:slug>/', views.DetailNewsView.as_view(), name='detail_news'),

]
