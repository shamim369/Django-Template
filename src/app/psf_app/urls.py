from django.urls import path
from .views import ProductAPIView, home, crudModelFormView

urlpatterns = [
    path('', home, name='home'),
    path('get_product/', ProductAPIView.as_view(), name='product_list'),


    path('model-form-crud/', crudModelFormView, name='crudModelFormView'),

]