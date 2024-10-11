from django.contrib import admin
from orders import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
