from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify
from tinymce.models import HTMLField
import math
from smart_selects.db_fields import ChainedForeignKey


class ProductType(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название', unique=True)

    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True, help_text='Заполнится при сохранении')
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_type', args=[self.slug])

    class Meta:
        verbose_name = 'Тип товаров'
        verbose_name_plural = 'Типы товаров'

    def __str__(self):
        return "%s" % self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductType, self).save(*args, **kwargs)


class Category(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Тип товара', related_name='categories')
    name = models.CharField(max_length=250, verbose_name='Название', unique=True)

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/categories/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')

    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True, help_text='Заполнится при сохранении')
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('category', args=[self.product_type.slug, self.slug])
    
    def get_cat_absolute_url(self):
        return reverse('products', args=[self.product_type.slug, self.slug, 'all'])

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

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/subcategories/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение', null=True, blank=True)

    slug = models.SlugField(max_length=250, verbose_name='Slug', help_text='Заполнится при сохранении')
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('products', args=[self.category.product_type.slug, self.category.slug, self.slug])

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return "%s" % self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)


class ProductSize(models.Model):
    value = models.CharField(max_length=10, verbose_name='Размер')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return "%s" % self.value


class ProductMaterial(models.Model):
    material = models.CharField(max_length=250, verbose_name='Материал')

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return "%s" % self.material


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Тип товара', related_name='products')
    category = ChainedForeignKey(Category, chained_field='product_type', chained_model_field='product_type', show_all=False, auto_choose=True, sort=True, verbose_name='Категория', related_name='products')
    subcategory = ChainedForeignKey(SubCategory, chained_field='category', chained_model_field='category', show_all=False, auto_choose=True, sort=True, verbose_name='Подкатегория', related_name='products', null=True, blank=True)
    name = models.CharField(max_length=250, verbose_name='Название')
    price_without_sale = models.PositiveIntegerField(default=0, verbose_name='Цена без скидки')
    # sale = models.PositiveIntegerField(default=0, verbose_name='Скидка')
    # price = models.PositiveIntegerField(default=0, verbose_name='Цена со скидкой', help_text='Заполнится при сохранении')
    materials = models.CharField(max_length=250, verbose_name='Материалы', default='', help_text='Пример: Кожа, Хлопок')
    sizes = models.CharField(max_length=250, verbose_name='Размеры', default='', help_text='Пример: 43, 44')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    features = models.CharField(max_length=250, verbose_name='Особенности')
    vendor_code = models.CharField(max_length=50, verbose_name='Артикул')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True, help_text='Заполнится при сохранении')
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    def get_main_image(self):
        return self.images.get(is_main=True)

    def get_absolute_url(self):
        if self.subcategory:
            subcategory = self.subcategory
        else:
            subcategory = 'all'
        return reverse('product_detail', args=[self.product_type.slug, self.category.slug, subcategory, self.slug])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '%s' % (self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category.name + '-' + self.name)
        # self.price = math.ceil(self.price_without_sale * (1 - self.sale / 100))

        # if not self.pk:
        #     Offer.objects.filter(product=self).delete()
        #     materials = self.materials.replace(',', '').split()
        #     sizes = self.sizes.replace(',', '').split()

        #     for size in sizes:
        #         for material in materials:
        #             Offer.objects.create(
        #                 product = self.id,
        #                 material = material,
        #                 size = size,
        #                 price_without_sale = self.price_without_sale,
        #             )
        
        super(Product, self).save(*args, **kwargs)


@receiver(post_save, sender=Product)
def create_all_offers(sender, instance, **kwargs):

    if not Offer.objects.filter(product=instance).exists():
        materials = instance.materials.replace(',', '').split()
        sizes = instance.sizes.replace(',', '').split()

        for size in sizes:
            for material in materials:
                Offer.objects.create(
                    product = instance,
                    material = material,
                    size = size,
                    price_without_sale = instance.price_without_sale,
                )


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='images')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/products/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    is_main = models.BooleanField(default=False, verbose_name='Главное изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return "%s" % self.id


class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='offers')
    material = models.CharField(max_length=250, verbose_name='Материал')
    size = models.CharField(max_length=250, verbose_name='Размер')
    price_without_sale = models.PositiveIntegerField(default=0, verbose_name='Цена без скидки')
    sale = models.PositiveIntegerField(default=0, verbose_name='Скидка')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена со скидкой', help_text='Заполнится при сохранении')
    stock = models.PositiveIntegerField(default=0, verbose_name='На складе')
    purchased = models.PositiveIntegerField(default=0, verbose_name='Куплено')

    class Meta:
        verbose_name = 'Вариант товаров'
        verbose_name_plural = 'Варианты товаров'
        unique_together = ('size', 'material', 'product')

    def save(self, *args, **kwargs):
        self.price = math.ceil(self.price_without_sale * (1 - self.sale / 100))
        super(Offer, self).save(*args, **kwargs)

    def __str__(self):
        return "%s-%s-%s-%s" % (self.product.name, self.material, self.size, self.price)


