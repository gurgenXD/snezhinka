from django.contrib import admin
from contacts.models import Phone, Schedule, Address, Fax, Email, MapCode


admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Fax)
admin.site.register(Email)
admin.site.register(Schedule)
admin.site.register(MapCode)