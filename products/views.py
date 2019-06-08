from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from products.models import Product, Category, ProductType, SubCategory, Offer, ProductMaterial, ProductSize


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
            products = Product.objects.filter(is_active=True, subcategory=subcategory)
        else:
            subcategory = category
            products = Product.objects.filter(is_active=True, category=category)
        
        offers = []
        for product in products:
            offers.append(min((item for item in product.offers.all()), key=lambda x:x.price))
                
        context = {
            'category': category,
            'product_type': product_type,
            'subcategory': subcategory,
            'offers': offers,
        }

        return render(request, 'products/products.html', context)


class ProductDetailView(View):
    def get(self, request, product_type_slug, category_slug, subcategory_slug, product_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        category = get_object_or_404(Category, slug=category_slug, product_type=product_type)
        product = get_object_or_404(Product, slug=product_slug, category=category, product_type=product_type)

        offers = product.offers.all()

        materials = list(set(item.material for item in offers))
        sizes = list(set(item.size for item in offers))

        first_material = materials[0]
        first_size = sizes[0]

        offer = Offer.objects.get(material=first_material, size=first_size, product=product)
        product_price_without_sale = offer.price_without_sale
        product_price = offer.price

        context = {
            'product': product,
            'materials': materials,
            'sizes': sizes,
            'first_material': first_material,
            'first_size': first_size,
            'product_price': product_price,
            'product_price_without_sale': product_price_without_sale,
        }

        return render(request, 'products/product_detail.html', context)


class ChangeProductProp(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        size_value = request.POST.get('size_value')
        material_value = request.POST.get('material_value')

        product = Product.objects.get(id=int(product_id))
        
        offer = Offer.objects.get(material=material_value, size=size_value, product=product)

        context = {
            'offer_price_without_sale': offer.price_without_sale,
            'offer_price': offer.price,
        }
    
        return JsonResponse(context)