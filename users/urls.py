from django.urls import path
from users import views
from landing.decorators import check_recaptcha


urlpatterns = [
    path('login/', check_recaptcha(views.LoginView.as_view()), name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('register/', check_recaptcha(views.RegisterView.as_view()), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('orders', views.UserOrdersView.as_view(), name='user_orders'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]