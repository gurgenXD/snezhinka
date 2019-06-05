from django.urls import path
from news import views


urlpatterns = [
    path('', views.NewsView.as_view(), name='news'),
    path('<news_slug>/', views.NewsDetailView.as_view(), name='news_detail'),
]