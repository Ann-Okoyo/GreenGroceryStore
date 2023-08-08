from django import forms
from .models  import Product



class ProductuploadForm(forms.ModelForm):
    class Meta:
        model = Product
        # will renderr all the fields
        fields = '__all__'