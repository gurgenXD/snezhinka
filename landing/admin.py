from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from adminsortable2.admin import SortableAdminMixin
from landing.models import ExtendedFlatPage, Agreement, AboutUs, OurPros, MailToString, MailFromString, TitleTag


admin.site.unregister(FlatPage)

@admin.register(ExtendedFlatPage)
class TinyMCEFlatPageAdmin(SortableAdminMixin, FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE())
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    
    list_display = ('title', 'url', 'my_order')
    list_display_links = ('title',)  
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


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):    
    fieldsets = (
        (None, {'fields': ('title', 'text')}),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('seo_title', 'desc', 'keywords'),
        }),
    )


admin.site.register(AboutUs)
admin.site.register(OurPros)
admin.site.register(MailToString)
admin.site.register(MailFromString)
admin.site.register(TitleTag)