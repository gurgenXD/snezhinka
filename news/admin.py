from django.contrib import admin
from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'short_desc', 'text', 'is_active', 'date')
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'desc', 'keywords'),
        }),
    )

    readonly_fields = ('slug',)