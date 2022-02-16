from urllib import response
from django.shortcuts import resolve_url
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from app.psf_app.views import home, ProductAPIView

# RUN - python manage.py test app.psf_app.tests.test_urls

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_url(self):
        # response = self.client.get('/psf/')
        # print(response)
        # self.assertEqual(response.status_code, 200)

        url = reverse('home')
        print(url)
        self.assertEquals(resolve(url).func, home)
    
    def test_url2(self):
        url = reverse('product_list')
        print(url)
        self.assertEquals(resolve(url).func.view_class, ProductAPIView)
