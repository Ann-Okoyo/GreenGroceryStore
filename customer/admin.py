from django.contrib import admin

# Register your models here.
from.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display= ("name","email","location","phone_number")
admin.site.register(Customer,CustomerAdmin)