from landing.models import ExtendedFlatPage
from contacts.models import Phone
from feedback.forms import CallBackForm
from products.models import ProductType


def header_info(request):
    points = ExtendedFlatPage.objects.all()
    if len(points) > 2:
        main_points = points[:2]
        drop_points = points[2:]
    elif len(points) <= 0:
        drop_points = []
        main_points = []
    else:
        drop_points = []
        main_points = points

    phone = Phone.objects.first()
    callback_form = CallBackForm()

    product_types = ProductType.objects.all()

    context = {
        'main_points': main_points,
        'drop_points': drop_points,
        'phone': phone,
        'callback_form': callback_form,
        'main_product_types': product_types,
    }

    return context