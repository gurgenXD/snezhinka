from django.urls import path
from orders import views


urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/address/', views.CarAddresstView.as_view(), name='cart_address'),
    path('cart/add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart/change_quantity/', views.ChangeQuantityView.as_view(), name='change_quantity'),
]