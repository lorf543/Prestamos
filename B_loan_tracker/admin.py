from django.contrib import admin

from .models import Customer,Lender,Receipt

# Register your models here.

admin.site.register(Customer)
admin.site.register(Lender)
admin.site.register(Receipt)
