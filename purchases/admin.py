from django.contrib import admin

# Register your models here.
from.models import Orders


class OrderAdmin(admin.ModelAdmin):
    list_display=("order_id","placement","order_status","number_of_orders","total_amount")
admin.site.register(Orders,OrderAdmin)








