from django.urls import path
from users import views
from landing.decorators import check_recaptcha


urlpatterns = [
    path('login/', check_recaptcha(views.LoginView.as_view()), name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('register/', check_recaptcha(views.RegisterView.as_view()), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('orders/', views.UserOrdersView.as_view(), name='user_orders'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('password-reset/', check_recaptcha(views.PasswordReset.as_view()), name='password_reset'),
    path('password-reset-done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password-reset-complete', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
]