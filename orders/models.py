from django.db import models
from users.models import User
from products.models import Offer


class Order(models.Model):
    PICKUP = 'pickup'
    DELIVERY = 'delivery'
    METHOD_OF_RECEIVING = [
        (PICKUP, 'Самовывоз'),
        (DELIVERY, 'Доставка'),
    ]

    SHIPPED = 'shipped'
    NOTSHIPPED = 'not_shipped'
    STATUS_DELIVERY = [
        (SHIPPED, 'Отгружено'),
        (NOTSHIPPED, 'Неотгружено'),
    ]

    # CASH = 'cash'
    # NOTCASH = 'not_cash'
    # PAYMENT = [
    #     (CASH, 'Наличный расчет'),
    #     (NOTCASH, 'Безналичный расчет'),
    # ]

    PAID = 'paid'
    NOTPAID = 'not_paid'
    STATUS_PAYMENT = [
        (PAID, 'Оплачено'),
        (NOTPAID, 'Неоплачено'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    full_name = models.CharField(max_length=250, verbose_name='ФИО', default='')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    postcode = models.CharField(max_length=20, verbose_name='Индекс', default='')
    country = models.CharField(max_length=250, default='Россия', verbose_name='Страна')
    region = models.CharField(max_length=250, verbose_name='Регион / Область', default='')
    locality = models.CharField(max_length=250, verbose_name='Город / Населённый пункт', default='')
    address = models.CharField(max_length=250, verbose_name='Улица, дом, квартира / офис', default='')
    
    total_price = models.PositiveIntegerField(default=0, verbose_name='Итоговая стоимость')
    delivery = models.CharField(max_length=250, choices=METHOD_OF_RECEIVING, verbose_name='Способ получения товара', default=PICKUP)
    status_delivery = models.CharField(max_length=250, choices=STATUS_DELIVERY, verbose_name='Статус доставки', default=NOTSHIPPED)
    # payment = models.CharField(max_length=250, choices=PAYMENT, verbose_name='Сбособ оплаты товара', default=CASH)
    status_payment = models.CharField(max_length=250, choices=STATUS_PAYMENT, verbose_name='Статус оплаты', default=NOTPAID)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    saved = models.BooleanField(default=False, verbose_name='Был сохранен')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ №%s' % self.id

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    # def save(self, *args, **kwargs):
    #     if self.status_payment.id != 1 and self.saved == False:
    #         for item in self.items.all():
    #             item.product.stock -= item.quantity
    #             item.product.save()
    #             self.saved = True
    #     super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='items')
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, verbose_name='Товар')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    total_price = models.PositiveIntegerField(default=0, verbose_name='Стоимость', help_text='Посчитается при сохранении.')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return "%s" % self.id

    def get_cost(self):
        return self.price * self.quantity
    
    # def save(self, *args, **kwargs):
    #     if self.order.status_payment.id != 1:   
    #         self.product.stock -= self.quantity
    #         self.product.save()
    #     super(OrderItem, self).save(*args, **kwargs)