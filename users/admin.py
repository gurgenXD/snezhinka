from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from users.models import User


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email', 'phone', 'postcode', 'country', 'region', 'locality', 'address')}),
        (_('Permissions'), {'classes': ('collapse', ), 'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'classes': ('collapse', ), 'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = ('country',)
    list_display = ('username', 'full_name', 'phone', 'email', 'is_active')


admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)