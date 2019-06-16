from django.urls import path
from products import views


urlpatterns = [
    path('products/<product_type_slug>/', views.ProductTypeView.as_view(), name='product_type'),
    path('products/<product_type_slug>/<category_slug>/', views.CategoryView.as_view(), name='category'),
    path('products/<product_type_slug>/<category_slug>/<subcategory_slug>/', views.ProductsView.as_view(), name='products'),
    path('products/<product_type_slug>/<category_slug>/<subcategory_slug>/<product_slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('change/prop/', views.ChangeProductProp.as_view(), name='change_prop'),

    path('sale/products/<product_type_slug>/', views.SaleProductTypeView.as_view(), name='sale_product_type'),
    path('sale/products/<product_type_slug>/<category_slug>/', views.SaleCategoryView.as_view(), name='sale_category'),
    path('sale/products/<product_type_slug>/<category_slug>/<subcategory_slug>/', views.SaleProductsView.as_view(), name='sale_products'),

    path('new/products/<product_type_slug>/', views.NewProductTypeView.as_view(), name='new_product_type'),
    path('new/products/<product_type_slug>/<category_slug>/', views.NewCategoryView.as_view(), name='new_category'),
    path('new/products/<product_type_slug>/<category_slug>/<subcategory_slug>/', views.NewProductsView.as_view(), name='new_products'),
]