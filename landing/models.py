from django.db import models
from django.contrib.flatpages.models import FlatPage
from tinymce.models import HTMLField


class ExtendedFlatPage(FlatPage):
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Сортировка')

    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    class Meta:
        verbose_name = 'Простая страница'
        verbose_name_plural = 'Простые страницы'
        ordering = ['my_order']


class Agreement(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = HTMLField(verbose_name='Текст')

    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    class Meta:
        verbose_name = 'Cоглашение на обработку персональных данных'
        verbose_name_plural = 'Cоглашение на обработку персональных данных'
    
    def __str__(self):
        return self.title