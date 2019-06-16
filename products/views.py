from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from products.models import Product, Category, ProductType, SubCategory, Offer, ProductMaterial, ProductSize


class ProductTypeView(View):
    def get(self, request, product_type_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        
        categories = Category.objects.filter(product_type=product_type)

        context = {
            'product_type': product_type,
            'categories': categories,
        }

        return render(request, 'products/product_type.html', context)



class SaleProductTypeView(View):
    def get(self, request, product_type_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)

        offers = Offer.objects.all()

        sale_offers = []
        for offer in offers:
            if offer.sale != 0:
                sale_offers.append(offer)
        
        products = Product.objects.filter(is_active=True, offers__in=sale_offers).distinct()
        sale_products = products.filter(product_type=product_type).distinct()
        categories = Category.objects.filter(products__in=sale_products).distinct()
        product_types = ProductType.objects.filter(products__in=products).distinct()

        context = {
            'product_type': product_type,
            'categories': categories,
            'len_sale_products': len(sale_products),
            'product_types': product_types,
        }

        return render(request, 'products/sale_product_type.html', context)


class NewProductTypeView(View):
    def get(self, request, product_type_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        
        products = Product.objects.filter(is_active=True, is_new=True).distinct()
        new_products = products.filter(product_type=product_type).distinct()
        categories = Category.objects.filter(products__in=new_products).distinct()
        product_types = ProductType.objects.filter(products__in=products).order_by('id').distinct()

        context = {
            'product_type': product_type,
            'categories': categories,
            'len_new_products': len(new_products),
            'product_types': product_types,
        }

        return render(request, 'products/new_product_type.html', context)



class CategoryView(View):
    def get(self, request, product_type_slug, category_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        category = get_object_or_404(Category, slug=category_slug, product_type=product_type)

       
        context = {
            'category': category,
            'product_type': product_type,
        }

        return render(request, 'products/category.html', context)


class SaleCategoryView(View):
    def get(self, request, product_type_slug, category_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        category = get_object_or_404(Category, slug=category_slug, product_type=product_type)

        offers = Offer.objects.all()

        sale_offers = []
        for offer in offers:
            if offer.sale != 0:
                sale_offers.append(offer)
        
        products = Product.objects.filter(is_active=True, offers__in=sale_offers).distinct()
        sale_products = products.filter(product_type=product_type, category=category).distinct()
        categories = Category.objects.filter(products__in=products, product_type=product_type).distinct()
        subcategories = SubCategory.objects.filter(products__in=sale_products).distinct()
        product_types = ProductType.objects.filter(products__in=products).distinct()
        
        
        context = {
            'category': category,
            'product_type': product_type,
            'categories': categories,
            'product_types': product_types,
            'subcategories': subcategories,
            'len_sale_category': len(sale_products),
        }

        return render(request, 'products/sale_category.html', context)


class NewCategoryView(View):
    def get(self, request, product_type_slug, category_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        category = get_object_or_404(Category, slug=category_slug, product_type=product_type)
        
        products = Product.objects.filter(is_new=True, is_active=True).distinct()
        new_products = products.filter(product_type=product_type, category=category).distinct()
        categories = Category.objects.filter(products__in=products, product_type=product_type).distinct()
        subcategories = SubCategory.objects.filter(products__in=new_products).distinct()
        product_types = ProductType.objects.filter(products__in=products).order_by('id').distinct()
        
        
        context = {
            'category': category,
            'product_type': product_type,
            'categories': categories,
            'product_types': product_types,
            'subcategories': subcategories,
            'len_new_category': len(new_products),
        }

        return render(request, 'products/new_category.html', context)



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


class SaleProductsView(View):
    def get(self, request, product_type_slug, category_slug, subcategory_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        category = get_object_or_404(Category, slug=category_slug, product_type=product_type)

        offers = Offer.objects.all()

        sale_offers = []
        for offer in offers:
            if offer.sale != 0:
                sale_offers.append(offer)

        products = Product.objects.filter(is_active=True, offers__in=sale_offers).distinct()
        sale_products = products.filter(product_type=product_type, category=category).distinct()

        if category.subcategories.all():
            subcategory = SubCategory.objects.get(slug=subcategory_slug, category=category)
            sale_products = sale_products.filter(subcategory=subcategory).distinct()
        else:
            subcategory = category

        categories = Category.objects.filter(products__in=products, product_type=product_type).distinct()
        subcategories = SubCategory.objects.filter(products__in=sale_products).distinct()
        product_types = ProductType.objects.filter(products__in=products).distinct()

        offers = []
        for product in sale_products:
            offers.append(min((item for item in product.offers.all()), key=lambda x:x.price))

                
        context = {
            'category': category,
            'product_type': product_type,
            'subcategory': subcategory,
            'offers': offers,
            'categories': categories,
            'product_types': product_types,
            'subcategories': subcategories,
            'len_sale_category': len(sale_products),
        }

        return render(request, 'products/sale_products.html', context)


class NewProductsView(View):
    def get(self, request, product_type_slug, category_slug, subcategory_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        category = get_object_or_404(Category, slug=category_slug, product_type=product_type)

        products = Product.objects.filter(is_active=True, is_new=True).distinct()
        new_products = products.filter(product_type=product_type, category=category).distinct()

        if category.subcategories.all():
            subcategory = SubCategory.objects.get(slug=subcategory_slug, category=category)
            new_products = new_products.filter(subcategory=subcategory).distinct()
        else:
            subcategory = category

        categories = Category.objects.filter(products__in=products, product_type=product_type).distinct()
        subcategories = SubCategory.objects.filter(products__in=new_products).distinct()
        product_types = ProductType.objects.filter(products__in=products).order_by('id').distinct()

        offers = []
        for product in new_products:
            offers.append(min((item for item in product.offers.all()), key=lambda x:x.price))

                
        context = {
            'category': category,
            'product_type': product_type,
            'subcategory': subcategory,
            'offers': offers,
            'categories': categories,
            'product_types': product_types,
            'subcategories': subcategories,
            'len_new_category': len(new_products),
        }

        return render(request, 'products/new_products.html', context)


class ProductDetailView(View):
    def get(self, request, product_type_slug, category_slug, subcategory_slug, product_slug):
        product_type = get_object_or_404(ProductType, slug=product_type_slug)
        category = get_object_or_404(Category, slug=category_slug, product_type=product_type)
        subcategory = SubCategory.objects.filter(slug=subcategory_slug, category=category)
        product = get_object_or_404(Product, slug=product_slug, category=category, product_type=product_type)

        offers = product.offers.all()

        materials = list(set(item.material for item in offers))
        sizes = list(set(item.size for item in offers))

        first_material = materials[0]
        first_size = sizes[0]

        offer = Offer.objects.get(material=first_material, size=first_size, product=product)
        product_price_without_sale = offer.price_without_sale
        product_price = offer.price

        similar_products = Product.objects.filter(is_active=True).exclude(id=product.id)
        similar_products = similar_products.filter(Q(subcategory__in=subcategory)|Q(category=category)|Q(product_type=product_type)).distinct()
        if len(similar_products) > 8:
            similar_products = similar_products[:8]

        similar_offers = []
        for product in similar_products:
            similar_offers.append(min((item for item in product.offers.all()), key=lambda x:x.price))

        context = {
            'product': product,
            'materials': materials,
            'sizes': sizes,
            'first_material': first_material,
            'first_size': first_size,
            'product_price': product_price,
            'product_price_without_sale': product_price_without_sale,
            'similar_offers': similar_offers,
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