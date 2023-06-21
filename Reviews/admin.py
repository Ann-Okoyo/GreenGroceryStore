from django.contrib import admin

# Register your models here.
from.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display=("Sender_Name","Message","Time_and_Date")
admin.site.register(Feedback,FeedbackAdmin)



