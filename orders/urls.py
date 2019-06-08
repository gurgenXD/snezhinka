from django.urls import path
from orders import views


urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    # path('cart/change_quantity/', views.change_quantity, name='change_quantity'),
]