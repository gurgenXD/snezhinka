from django.urls import path
from orders import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('cart/', login_required(views.CartView.as_view()), name='cart'),
    path('cart/address/', login_required(views.CarAddressView.as_view()), name='cart_address'),
    path('pickup/', login_required(views.PickUpView.as_view()), name='pickup'),
    path('delivery/', login_required(views.DeliveryView.as_view()), name='delivery'),
    path('cart/add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/', login_required(views.RemoveFromCartView.as_view()), name='remove_from_cart'),
    path('cart/change_quantity/', login_required(views.ChangeQuantityView.as_view()), name='change_quantity'),
]