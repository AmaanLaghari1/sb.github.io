from django import forms 
from .models import Product, PlacedOrder, Pimage, ProRating



class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'sub_category', 'bulk_quantity', 'bulk_price', 'price', 'description', 'seller_contact']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control is-valid', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control is-valid', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select is-valid'}),
            'sub_category': forms.Select(attrs={'class': 'form-select is-valid'}),
            'price': forms.TextInput(attrs={'type': 'number', 'class': 'form-control is-valid'}),
            'bulk_quantity': forms.TextInput(attrs={'type': 'number', 'class': 'form-control is-valid'}),
            'bulk_price': forms.TextInput(attrs={'type': 'number', 'class': 'form-control is-valid'}),  
            'seller_contact': forms.NumberInput(attrs={'class': 'form-control is-valid'}),  
            'pub_date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control is-valid'})
        }
        labels = {'bulk_quantity': 'Bulk Products(if any)', 'bulk_price': 'Bulk Products Price(if any)', 'sub_category': 'Sub-category(if any)'}

class RateForm(forms.ModelForm):
    class Meta:
        model = ProRating
        fields = ['review', 'rate']

class PimgForm(forms.ModelForm):
    # images = forms.FileInput(attrs={'type': 'file', 'class': 'form-control', 'multiple': True})
    class Meta:
        model = Pimage
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'type': 'file', 'class': 'form-control', 'multiple': True, 'required': True})
        }
        labels = {'image': 'Add Images(High quality recommended)'}

class ConfirmOrderForm(forms.ModelForm):
    class Meta:
        model = PlacedOrder
        fields = ['contact', 'address', 'address2', 'country', 'city', 'zip_code']
        widgets = {
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"1234 Main St"}),
            'address2': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"1234 Main St"}),
            'country': forms.Select(attrs={'class': 'form-control', 'required': False, 'value': 'Pakistan'}),
            'city': forms.Select(attrs={'class': 'form-control', 'required': False, 'value': 'Hyderabad'}),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control'}),
        }
