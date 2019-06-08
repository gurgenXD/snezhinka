from django.contrib import admin
from products.models import Product, Offer, Image, Category, SubCategory, ProductMaterial, ProductSize, ProductType


class OfferInline(admin.TabularInline):
    model = Offer
    extra = 0
    readonly_fields = ('material', 'size', 'purchased', 'price',)
    can_delete = False
    fields = ('material', 'size', 'price_without_sale', 'sale', 'price', 'stock', 'purchased')
    classes = ('grp-collapse grp-closed',)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    classes = ('grp-collapse grp-closed',)


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0
    readonly_fields = ('slug',)
    classes = ('grp-collapse grp-closed',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('product_type', 'category', 'subcategory', 'name', 'price_without_sale', 'materials', 'sizes',
            'description', 'features', 'color', 'vendor_code', 'is_active'),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'desc', 'keywords'),
        }),
    )

    readonly_fields = ('slug',)
    inlines = (ImageInline, OfferInline)
    list_filter = ('product_type', 'category', 'subcategory')
    list_display = ('name', 'product_type', 'category', 'subcategory', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('product_type', 'name', 'image'),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'desc', 'keywords'),
        }),
    )

    inlines = (SubCategoryInline,)
    readonly_fields = ('slug',)


# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {
#             'fields': ('product_type', 'category', 'name',),
#         }),
#         ('SEO', {
#             'classes': ('grp-collapse grp-closed',),
#             'fields': ('slug', 'seo_title', 'desc', 'keywords'),
#         }),
#     )
    
#     list_display = ('name', 'category')
#     list_filter = ('category',)
#     readonly_fields = ('slug',)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
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


admin.site.register(ProductMaterial)
admin.site.register(ProductSize)