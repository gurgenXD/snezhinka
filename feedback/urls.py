from django.urls import path
from feedback import views
from landing.decorators import check_recaptcha


urlpatterns = [
    path('call/', views.CallBackView.as_view(), name='callback'),
    path('message/', check_recaptcha(views.FeedBackView.as_view()), name='feedback'),
]