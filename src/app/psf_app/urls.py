from django.urls import path
from .views import ProductAPIView

urlpatterns = [
    path('get_product/', ProductAPIView.as_view()),
]