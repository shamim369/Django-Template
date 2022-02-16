from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer

class ProductAPIView(APIView):

    def get(self, request):
        s = request.GET.get('s')
        sort = request.GET.get('sort')

        products = Product.objects.all()

        if s:
            products = products.filter(
                Q(title__icontains=s) | Q(description__icontains=s)
            )
        if sort == 'asc':
            products = products.order_by('price')
        elif sort == 'desc':
            products = products.order_by('-price')


        product_serializers = ProductSerializer(products, many=True)
        return Response(product_serializers.data)