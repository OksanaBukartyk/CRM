from django import forms
from .models import Buyer, Seller, Selling, Product

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['first_name', 'last_name', 'phone_number', 'email']  # List the fields you want to edit


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'date_employment', 'position'] 


class SellingForm(forms.ModelForm):
    class Meta:
        model = Selling
        fields = ['buyer', 'seller', 'product', 'date_sale', 'amount_sale'] 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'count'] 