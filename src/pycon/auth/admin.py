from django.contrib import admin

from pycon.auth.models import EndUser, CustomerGroup


class CustomerGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomerGroup, CustomerGroupAdmin)
admin.site.register(EndUser, CustomerGroupAdmin)
