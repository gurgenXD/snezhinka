from django.db import models
from django.contrib.flatpages.models import FlatPage


class ExtendedFlatPage(FlatPage):
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    class Meta:
        verbose_name = 'Простая страница'
        verbose_name_plural = 'Простые страницы'