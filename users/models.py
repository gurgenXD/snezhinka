from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=250, verbose_name='ФИО', null=True, blank=True, default='')
    email = models.EmailField(max_length=250, verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Телефон', null=True, blank=True, default='')
    postcode = models.CharField(max_length=20, verbose_name='Индекс', null=True, blank=True, default='')
    country = models.CharField(max_length=250, verbose_name='Страна', null=True, blank=True, default='Россия')
    region = models.CharField(max_length=250, verbose_name='Регион / Область', null=True, blank=True, default='')
    locality = models.CharField(max_length=250, verbose_name='Город / Населённый пункт', null=True, blank=True, default='')
    address = models.CharField(max_length=250, verbose_name='Улица, дом, квартира / офис', null=True, blank=True, default='')

    def __str__(self):
        return '%s' % self.full_name