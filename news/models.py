from django.db import models
from datetime import date
from django.urls import reverse
from slugify import slugify
from tinymce.models import HTMLField


class News(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name='Название')
    text = HTMLField(verbose_name='Текст')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    date = models.DateField(default=date.today, verbose_name='Дата создания')

    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True, help_text='Заполнится при сохранении')
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/news/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        print(self.slug)
        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return '%s' % self.title