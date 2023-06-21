from django.db import models

# Create your models here.


class Notify(models.Model):
    Sender_Name=models.CharField(max_length=32)
    Title=models.CharField(max_length=32)
    Description=models.CharField(max_length=32)
    Message=models.CharField(max_length=32)
    Time_and_Date=models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.name

