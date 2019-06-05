from django.urls import path
from landing import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('users_content/', views.UsersContentView.as_view(), name='users_content'),
]