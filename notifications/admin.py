from django.contrib import admin

# Register your models here.
from.models import Notify

class NotifyAdmin(admin.ModelAdmin):
    list_display=("Sender_Name","Title","Description","Message","Time_and_Date")
admin.site.register(Notify,NotifyAdmin)


