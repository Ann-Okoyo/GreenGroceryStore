from django.contrib import admin

# Register your models here.
from.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display =("date","delivery_options","delivery_date")
admin.site.register(Order,OrderAdmin)








