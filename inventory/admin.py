
from django.contrib import admin
from.models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","stock","price","date_created","description","image","date_updated")
admin.site.register(Product,ProductAdmin)
