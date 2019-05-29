from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from landing.models import ExtendedFlatPage


admin.site.unregister(FlatPage)

@admin.register(ExtendedFlatPage)
class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE())
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        ('Расширенные настройки', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('registration_required', 'template_name'),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('seo_title', 'desc', 'keywords'),
        }),
    )



