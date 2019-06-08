from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from orders.cart import Cart
from products.models import Product, ProductSize, ProductMaterial, Offer


class CartView(View):
    def get(self, request):

        context = {
            # 'product_type': product_type,
        }

        return render(request, 'orders/cart.html', context)


class AddToCartView(View):
    def post(self, request):
        cart = Cart(request)
        
        product_id = request.POST.get('product_id')
        qty = request.POST.get('qty', 1)
        size_value = request.POST.get('size_value')
        material_value = request.POST.get('material_value')

        product = Product.objects.get(id=int(product_id))
        size = ProductSize.objects.get(value=size_value)
        material = ProductMaterial.objects.get(material=material_value)
        cart.add(product, int(qty))

        try:
            offer = Offer.objects.get(material=material, size=size, product=product)
            cart.add(offer, int(qty), )
        except Offer.DoesNotExist:
            cart.add(offer, int(qty))

        context = {
            'cart_len': len(cart),
            # 'total_price': cart.get_total_price(),
        }

        return JsonResponse(context)


class RemoveFromCartView(View):
    def get(self, request):

        context = {
            # 'product_type': product_type,
        }

        return render(request, 'orders/cart.html', context)