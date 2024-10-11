from django.shortcuts import render
from rest_framework import viewsets, mixins
from orders.models import Product
from orders.serializers import ProductListSerializer


class ProductAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
