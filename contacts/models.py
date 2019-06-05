from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=250, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return '%s' % self.address


class Phone(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return '%s' % self.phone


class Fax(models.Model):
    fax = models.CharField(max_length=20, verbose_name='Факс')

    class Meta:
        verbose_name = 'Факс'
        verbose_name_plural = 'Факсы'

    def __str__(self):
        return '%s' % self.fax


class Email(models.Model):
    email = models.CharField(max_length=250, verbose_name='E-mail')

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mail'

    def __str__(self):
        return '%s' % self.email


class MapCode(models.Model):
    map_code = models.TextField(verbose_name='Карта')

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return '%s' % self.map_code


class Schedule(models.Model):
    days_point = models.CharField(max_length=250, verbose_name='Дни недели')
    time_point = models.CharField(max_length=250, verbose_name='Время работы')

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Режим работы'

    def __str__(self):
        return '%s %s' % (self.days_point, self.time_point)