from django import forms
from .models import Customer


 class CustommeruploadForm(forms.ModelForm):

    class Meta:
        models = Customer

        fields =  "__all__"