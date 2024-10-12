from django.contrib import admin
from orders import models
from django.utils.html import format_html
from orders.models import PaymentStatus, OrderStatus


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time_confirmation', 'confirm_order_button',)
    exclude = ('status',)

    def confirm_order_button(self, order):
        if order.status == OrderStatus.Confirmed:
            return 'Недоступно, заказ уже подтвержден'
        if hasattr(order, 'payment') and order.payment.status == PaymentStatus.Paid:
            return format_html('<a class="button" href="{}">Подтвердить</a>', f'/confirm_order/{order.id}')
        return 'Недоступно, заказ не оплачен'

    confirm_order_button.short_description = 'Подтверждение'
    confirm_order_button.allow_tags = True


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('amount', 'order', 'status', 'type')
