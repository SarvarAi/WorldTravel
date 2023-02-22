from django.contrib import admin
from .models import EmailSubscription, InfoPages, PageCategory


# Register your models here.
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_display_links = ['email']


class InfoPagesAdmin(admin.ModelAdmin):
    list_display = ['page', 'information']
    list_display_links = ['page', 'information']


class PageCategoryAdmin(admin.ModelAdmin):
    list_display = ['page']
    list_display_links = ['page']


admin.site.register(PageCategory, PageCategoryAdmin)
admin.site.register(EmailSubscription, EmailSubscriptionAdmin)
admin.site.register(InfoPages, InfoPagesAdmin)
