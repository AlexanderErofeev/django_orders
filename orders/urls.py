from django.urls import path, include
from rest_framework.routers import SimpleRouter

from orders import views

api_router = SimpleRouter()
api_router.register(r'products', views.ProductAPIView, basename='products')

urlpatterns = [
    path('api/', include(api_router.urls)),
]
