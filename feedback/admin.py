from django.contrib import admin
from feedback.models import FeedBack, CallBack


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ('phone', 'date')


@admin.register(FeedBack)
class FeedBackkAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date')
