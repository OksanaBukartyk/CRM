from django.db import models

class Buyer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Seller(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    date_employment = models.DateField()
    
    SELLER_POSITION_CHOICES = (
        ('0', 'Легко'),
        ('1', 'Нормально'),
        ('3', 'Складно'),
    )
    position = models.CharField(max_length=100, choices=SELLER_POSITION_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    count = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.product_name


class Selling(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_sale = models.DateField()
    amount_sale = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Продаж {self.date_sale} на суму {self.amount_sale}"
