from django.contrib import admin
from products.models import Product, Offer, Image, Category, SubCategory, ProductMaterial, ProductSize


class OfferInline(admin.TabularInline):
    model = Offer
    extra = 0
    readonly_fields = ('purchased', 'price',)
    fields = ('material', 'size', 'price_without_sale', 'sale', 'price', 'stock', 'purchased', 'is_active')
    classes = ('grp-collapse grp-closed',)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    classes = ('grp-collapse grp-closed',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('category', 'subcategory', 'name', 'description', 'features', 'color', 'vendor_code'),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'desc', 'keywords'),
        }),
    )

    readonly_fields = ('slug',)
    inlines = (ImageInline, OfferInline,)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'desc', 'keywords'),
        }),
    )

    readonly_fields = ('slug',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('category', 'name',),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'desc', 'keywords'),
        }),
    )

    readonly_fields = ('slug',)


admin.site.register(ProductMaterial)
admin.site.register(ProductSize)