from django.db import models
from django_enum import EnumField


class OrderStatus(models.TextChoices):
    Confirmed = 'Confirmed'
    Unconfirmed = 'Unconfirmed'


class PaymentStatus(models.TextChoices):
    Paid = 'Paid'
    Unpaid = 'Unpaid'


class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    image = models.ImageField('Картинка', upload_to='product_images', null=True, blank=True)
    content = models.TextField('Контент', null=True, blank=True)
    price = models.FloatField('Стоимость')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    total_amount = models.FloatField('Итоговая сумма')
    status = EnumField(OrderStatus, default=OrderStatus.Unconfirmed, blank=True)
    date_time_create = models.DateTimeField('Время создания', auto_now_add=True)
    date_time_confirmation = models.DateTimeField('Время подтверждения', null=True, blank=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Payment(models.Model):
    amount = models.FloatField('Сумма')
    status = EnumField(PaymentStatus, default=PaymentStatus.Unpaid, blank=True)
    type = models.CharField('Тип оплаты', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
