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
        quantity = request.POST.get('quantity', 1)
        size_value = request.POST.get('size_value')
        material_value = request.POST.get('material_value')

        product = Product.objects.get(id=int(product_id))
        offer = Offer.objects.get(material=material_value, size=size_value, product=product)
        cart.add(offer, int(quantity))

        context = {
            'cart_len': len(cart),
        }

        return JsonResponse(context)


class RemoveFromCartView(View):
    def get(self, request):
        cart = Cart(request)
        offer_id = request.GET.get('offer_id')

        offer = Offer.objects.get(id=int(offer_id))
        cart.remove(offer)

        total_price = cart.get_total_price()
        cart_len = len(cart)

        context = {
            'offer_id': offer.id,
            'total_price': total_price,
            'cart_len': cart_len,
        }

        return JsonResponse(context)


class ChangeQuantityView(View):
    def get(self, request):
        cart = Cart(request)
        offer_id = request.GET.get('offer_id')
        quantity = request.GET.get('quantity')

        offer = Offer.objects.get(id=int(offer_id))
        cart.change_quantity(offer, int(quantity))

        offer_cost = offer.price * int(quantity)
        total_price = cart.get_total_price()
        cart_len = len(cart)

        context = {
            'offer_cost': offer_cost,
            'total_price': total_price,
            'cart_len': cart_len,
        }

        return JsonResponse(context)