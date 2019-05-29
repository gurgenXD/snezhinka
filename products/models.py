from django.db import models
from django.urls import reverse
from slugify import slugify
from tinymce.models import HTMLField
import math


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название', unique=True)

    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True, help_text='Заполнится при сохранении')
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return "%s" % self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='subcategories')
    name = models.CharField(max_length=250, verbose_name='Название')

    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True, help_text='Заполнится при сохранении')
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('subcategory', args=[self.category.slug, self.slug])

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return "%s" % self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + '-' + self.id)
        super(SubCategory, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    name = models.CharField(max_length=250, verbose_name='Название')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    features = models.CharField(max_length=250, verbose_name='Особенности')
    vendor_code = models.CharField(max_length=50, verbose_name='Артикул')
    description = HTMLField(verbose_name='Описание')

    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True, help_text='Заполнится при сохранении')
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    def get_main_image(self):
        return self.images.get(is_main=True)

    def get_absolute_url(self):
        return reverse('product', args=[self.category.slug, self.subcategory.slug, self.slug])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '%s' % (self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + '-' + self.id)
        super(Product, self).save(*args, **kwargs)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='images')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/products/%s/%s' % (self.product.slug, filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    is_main = models.BooleanField(default=False, verbose_name='Главное изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return "%s" % self.id


class ProductSize(models.Model):
    size = models.PositiveSmallIntegerField(verbose_name='Размер')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return "%s" % self.size


class ProductMaterial(models.Model):
    material = models.CharField(max_length=250, verbose_name='Материал')

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return "%s" % self.material


class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='offers')
    material = models.ForeignKey(ProductMaterial, on_delete=models.CASCADE, verbose_name='Материал', related_name='offers')
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, verbose_name='Размер', related_name='offers')
    price_without_sale = models.PositiveIntegerField(default=0, verbose_name='Цена без скидки')
    sale = models.PositiveIntegerField(default=0, verbose_name='Скидка')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена со скидкой', help_text='Заполнится при сохранении')
    stock = models.PositiveIntegerField(default=0, verbose_name='На складе')
    purchased = models.PositiveIntegerField(default=0, verbose_name='Куплено')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Вариант товаров'
        verbose_name_plural = 'Варианты товаров'

    def save(self, *args, **kwargs):
        self.price = math.ceil(self.price_without_sale * (1 - self.sale / 100))
        super(Offer, self).save(*args, **kwargs)

    def __str__(self):
        return "%s-%s-%s-%s" % (self.product.name, self.material.material, self.size.size, self.price)


