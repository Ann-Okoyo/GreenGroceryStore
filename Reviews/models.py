from django.db import models

# Create your models here.
class Feedback(models.Model):
    Sender_Name=models.CharField(max_length=32)
    Message=models.TextField()
    Time_and_Date=models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.Sender_Name


