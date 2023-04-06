from django.contrib import admin

from stockapp.models import Login, Customer, Stock

# Register your models here.
admin.site.register(Login)
admin.site.register(Customer)
admin.site.register(Stock)