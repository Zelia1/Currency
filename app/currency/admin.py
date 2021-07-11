from currency.models import Banks, ContactUs, Rate

from django.contrib import admin


class BankAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'url',
        'email_from',
        'number_phone',
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'name',
    )


admin.site.register(Banks, BankAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'message',
    )
    list_filter = (
        'subject',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(ContactUs, ContactUsAdmin)


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sale',
        'buy',
        'type',
        'created',
        'source',
    )


admin.site.register(Rate, RateAdmin)
