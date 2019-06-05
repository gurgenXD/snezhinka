from django.shortcuts import render, get_object_or_404
from django.views import View
from products.models import Product, Category, ProductType, SubCategory, Offer


class ProductTypeView(View):
    def get(self, request, product_type_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)

        context = {
            'product_type': product_type,
        }

        return render(request, 'products/product_type.html', context)


class CategoryView(View):
    def get(self, request, product_type_slug, category_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        category = get_object_or_404(Category, slug=category_slug, product_type=product_type)
        
        context = {
            'category': category,
            'product_type': product_type,
        }

        return render(request, 'products/category.html', context)


class ProductsView(View):
    def get(self, request, product_type_slug, category_slug, subcategory_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        category = get_object_or_404(Category, slug=category_slug, product_type=product_type)
        if category.subcategories.all():
            subcategory = SubCategory.objects.get(slug=subcategory_slug, category=category)
        else:
            subcategory = category
        
        context = {
            'category': category,
            'product_type': product_type,
            'subcategory': subcategory,
        }

        return render(request, 'products/products.html', context)


class ProductDetailView(View):
    def get(self, request, product_type_slug, category_slug, subcategory_slug, product_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        category = get_object_or_404(Category, slug=category_slug, product_type=product_type)
        product = get_object_or_404(Product, slug=product_slug, category=category, product_type=product_type)
        
        context = {
            'product': product,
        }

        return render(request, 'products/product_detail.html', context)
