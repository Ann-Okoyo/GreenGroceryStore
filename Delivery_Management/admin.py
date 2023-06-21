from django.contrib import admin

# Register your models here.
from .models import Delivery_Person

class Delivery_PersonAdmin(admin.ModelAdmin):
    list_display=("name","location","Phone_Number","Price")
admin.site.register(Delivery_Person,Delivery_PersonAdmin)



