from django.db import models
from django.contrib.flatpages.models import FlatPage


class ExtendedFlatPage(FlatPage):
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Сортировка')

    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    class Meta:
        verbose_name = 'Простая страница'
        verbose_name_plural = 'Простые страницы'
        ordering = ['my_order']