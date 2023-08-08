from django import forms
from .models import Basket



class CartuploadForm(forms.ModelForm):
    class Meta:
        model = Basket
        # will renderr all the fields
        fields = '__all__'