from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from orders.cart import Cart
from products.models import Product, ProductSize, ProductMaterial, Offer
from contacts.models import Phone, Schedule, Address, MapCode
from orders.forms import PickUpForm, DeliveryForm
from orders.models import OrderItem
from landing.models import MailToString


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


class CarAddressView(View):
    def get(self, request):
        phones = Phone.objects.all()
        shedules = Schedule.objects.all()
        addresses = Address.objects.all()
        map_code = MapCode.objects.first()

        user = request.user

        pickup_form = PickUpForm(user)
        delivery_form = DeliveryForm(user)

        context = {
            'phones': phones,
            'shedules': shedules,
            'addresses': addresses,
            'map_code': map_code,
            'pickup_form': pickup_form,
            'delivery_form': delivery_form,
        }

        return render(request, 'orders/cart_address.html', context)


class PickUpView(View):
    def post(self, request):
        cart = Cart(request)
        user = request.user
        pickup_form = PickUpForm(user, request.POST)
        
        if pickup_form.is_valid():
            new_order = pickup_form.save(commit=False)
            new_order.user = user
            new_order.total_price = cart.get_total_price()
            
            user.phone = pickup_form.cleaned_data.get('phone')
            user.save()
            
            new_order.delivery = new_order.PICKUP
            new_order.save()
        else:
            return redirect('cart_address')
        
        for item in cart:
            offer = Offer.objects.get(id=int(item['offer_id']))
            OrderItem.objects.create(
                order=new_order,
                offer=offer,
                price=item['price'],
                quantity=item['quantity'],
                total_price=item['cost']
            )

        current_site = get_current_site(request)
        mail_subject = 'Новый заказ на сайте: ' + current_site.domain
        message = render_to_string('orders/new_order_message.html', {
            'domain': current_site.domain,
            'order': new_order,
        })
        to_email = MailToString.objects.first().email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        cart.clear()

        return render(request, 'orders/cart_success.html', {})


class DeliveryView(View):
    def post(self, request):
        cart = Cart(request)
        user = request.user
        delivery_form = DeliveryForm(user, request.POST)

        if delivery_form.is_valid():
            new_order = delivery_form.save(commit=False)
            new_order.user = user
            new_order.total_price = cart.get_total_price()

            user.phone = delivery_form.cleaned_data.get('phone')
            user.full_name = delivery_form.cleaned_data.get('full_name')
            user.postcode = delivery_form.cleaned_data.get('postcode')
            user.region = delivery_form.cleaned_data.get('region')
            user.locality = delivery_form.cleaned_data.get('locality')
            user.address = delivery_form.cleaned_data.get('address')
            user.save()

            new_order.delivery = new_order.DELIVERY
            new_order.save()
        else:
            return redirect('cart_address')
        
        for item in cart:
            offer = Offer.objects.get(id=int(item['offer_id']))
            OrderItem.objects.create(
                order=new_order,
                offer=offer,
                price=item['price'],
                quantity=item['quantity'],
                total_price=item['cost']
            )
        
        current_site = get_current_site(request)
        mail_subject = 'Новый заказ на сайте: ' + current_site.domain
        message = render_to_string('orders/new_order_message.html', {
            'domain': current_site.domain,
            'order': new_order,
        })
        to_email = MailToString.objects.first().email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        cart.clear()

        return render(request, 'orders/cart_success.html', {})