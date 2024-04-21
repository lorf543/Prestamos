from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

import random
import string

# Create your models here.

class Lender(AbstractUser):
    id_lender = models.CharField(max_length=50, null=True, blank=True,unique=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            code = self.generate_unique_code()
            self.id_lender = code
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        code = 'L-' + ''.join(random.choice(string.digits) for _ in range(9))
        while Lender.objects.filter(id_lender=code).exists(): 
            code = 'L-' + ''.join(random.choice(string.digits) for _ in range(9))  
        return code

    
    
    

class Product(models.Model):
    id_product = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    total_amount = models.IntegerField()
    total_amount_pending = models.IntegerField()
    n_quotas = models.IntegerField()
    n_quotas_made = models.IntegerField()
    total_payed = models.IntegerField()
    total_pending = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    next_payment_date = models.DateField()
    date_closed = models.DateField()
    date_open = models.DateField()
    date_late = models.DateField()
    product_state = models.CharField(max_length=50)
    payment_frequency = models.CharField(max_length=50)

    date_added = models.DateField()
    date_update = models.DateField()
    added_by = models.ForeignKey(Lender, on_delete=models.CASCADE, related_name="product_added")
    update_by = models.ForeignKey(Lender, on_delete=models.CASCADE, related_name="product_update")

class Receipt(models.Model):
    id_receipt = models.CharField(max_length=50)
    amount = models.IntegerField()
    n_quotas = models.IntegerField()
    n_quotas_made = models.IntegerField()
    total_payed = models.IntegerField()
    total_pending = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    next_payment_date = models.DateField()

    date_added = models.DateField()
    date_update = models.DateField()
    added_by = models.ForeignKey(Lender, on_delete=models.CASCADE, related_name="receipt_added")
    update_by = models.ForeignKey(Lender, on_delete=models.CASCADE, related_name="receipt_update")

class Customer(models.Model):
    id_customer = models.CharField(max_length=50)
    name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField()
    phone = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE, related_name="customer_lender")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="customer_product")
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name="customer_receipt")

    date_added = models.DateField()
    date_update = models.DateField()
    added_by = models.ForeignKey(Lender, on_delete=models.CASCADE, related_name="customer_added")
    update_by = models.ForeignKey(Lender, on_delete=models.CASCADE, related_name="customer_update")

