from django.contrib import admin

# Register your models here.
from.models import Shipment


class ShipmentAdmin(admin.ModelAdmin):
    list_display=("Portname","Date_of_Shipment_Placed","Date_of_Receive_Shipment","Product")
admin.site.register(Shipment,ShipmentAdmin)




