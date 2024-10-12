from django.urls import path, include
from rest_framework.routers import SimpleRouter

from orders import views

api_router = SimpleRouter()
api_router.register(r'products', views.ProductAPIView, basename='products')
api_router.register(r'orders', views.OrderCreateAPIView, basename='orders')
api_router.register(r'product', views.PaymentCreateAPIView, basename='product')

urlpatterns = [
    path('api/', include(api_router.urls)),
]
