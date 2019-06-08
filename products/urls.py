from django.urls import path
from products import views


urlpatterns = [
    path('products/<product_type_slug>/', views.ProductTypeView.as_view(), name='product_type'),
    path('products/<product_type_slug>/<category_slug>/', views.CategoryView.as_view(), name='category'),
    path('products/<product_type_slug>/<category_slug>/<subcategory_slug>/', views.ProductsView.as_view(), name='products'),
    path('products/<product_type_slug>/<category_slug>/<subcategory_slug>/<product_slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('change/prop/', views.ChangeProductProp.as_view(), name='change_prop'),
]