from django.urls import path
from .views import ProductAPIView, home

urlpatterns = [
    path('', home, name='home'),
    path('get_product/', ProductAPIView.as_view(), name='product_list'),
]