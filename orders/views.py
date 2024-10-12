from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from orders.models import Product, Order, Payment
from orders.serializers import ProductListSerializer, CreateOrderSerializer, OrderSerializer, CreatePaymentSerializer, \
    PaymentSerializer
from django.core.exceptions import BadRequest
from drf_spectacular.utils import extend_schema


class ProductAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


@extend_schema(responses=OrderSerializer)
class OrderCreateAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateOrderSerializer

    def create(self, request, *args, **kwargs):
        product_ids = request.data.get('products')
        corrent_products_dict = dict(Product.objects.filter(id__in=product_ids).values_list('id', 'price'))

        if not set(corrent_products_dict.keys()) == set(product_ids):
            not_found_ids = set(product_ids) - set(corrent_products_dict.keys())
            raise BadRequest(f"Not Found ids: {', '.join(map(str, not_found_ids))}")

        total_amount = sum(corrent_products_dict[id] for id in product_ids)
        order = Order.objects.create(total_amount=total_amount)
        return Response(OrderSerializer(order).data)


@extend_schema(responses=PaymentSerializer)
class PaymentCreateAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CreatePaymentSerializer

    def create(self, request, *args, **kwargs):
        order_id = request.data.get('order')
        order = get_object_or_404(Order, id=order_id)

        payment = Payment.objects.create(amount=order.total_amount)
        return Response(PaymentSerializer(payment).data)
