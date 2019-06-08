from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('total_price',)
    fields = ('product', 'price', 'quantity', 'total_price')
    classes = ('grp-collapse grp-closed',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('user', 'full_name', 'email', 'phone', 'postcode', 'country', 'region', 'locality',
            'address', 'delivery', 'status_delivery', 'status_payment'),
        }),
        ('Информация о заказе', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('total_price', 'created', 'updated'),
        }),
    )

    readonly_fields = ('total_price', 'created', 'updated')
    inlines = (OrderItemInline,)
