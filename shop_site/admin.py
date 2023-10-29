from django.contrib import admin

# Register your models here.


from .models import Buyer, Seller, Selling, Product
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Selling)
admin.site.register(Product)
