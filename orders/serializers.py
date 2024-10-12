from rest_framework import serializers
from orders.models import Product, Order, Payment


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class CreateOrderSerializer(serializers.Serializer):
    products = serializers.ListField(
        child=serializers.IntegerField(min_value=0)
    )

    def to_representation(self, data):
        return OrderSerializer(context=self.context).to_representation(data)


class CreatePaymentSerializer(serializers.Serializer):
    order = serializers.IntegerField(min_value=0)

    def to_representation(self, data):
        return PaymentSerializer(context=self.context).to_representation(data)
