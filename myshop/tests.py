from decimal import Decimal
from django.test import TestCase, SimpleTestCase
from .models import Category, Product


# тест моделей в myshop/models.py
class CategoryModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Phone', slug='phone')

    def test_category_name(self):
        result = Category.objects.get(id=1)
        field_label = result._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_category_name_max_length(self):
        result = Category.objects.get(id=1)
        max_length = result._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_category_slug(self):
        result = Category.objects.get(id=1)
        field_label = result._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_category_slug_max_length(self):
        result = Category.objects.get(id=1)
        max_length = result._meta.get_field('slug').max_length
        self.assertEquals(max_length, 100)

    def test_category_get_absolute_url(self):
        result = Category.objects.get(id=1)
        self.assertEquals(result.get_absolute_url(), '/phone/')


class ProductModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='products')
        Product.objects.create(
            category=category,
            name='test',
            slug='test',
            description='test',
            price=Decimal('123.456')
        )

    def test_product_name(self):
        result = Product.objects.get(id=1)
        field_label = result._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_product_name_max_length(self):
        result = Product.objects.get(id=1)
        max_length = result._meta.get_field('name').max_length
        self.assertEquals(max_length, 150)

    def test_product_slug(self):
        result = Product.objects.get(id=1)
        field_label = result._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_product_slug_max_length(self):
        result = Product.objects.get(id=1)
        max_length = result._meta.get_field('slug').max_length
        self.assertEquals(max_length, 150)

    def test_product_description(self):
        result = Product.objects.get(id=1)
        field_label = result._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_product_description_max_length(self):
        result = Product.objects.get(id=1)
        max_length = result._meta.get_field('description').max_length
        self.assertEquals(max_length, 1000)

    def test_product_price(self):
        result = Product.objects.get(id=1)
        field_label = result._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_product_get_absolute_url(self):
        result = Product.objects.get(id=1)
        self.assertEquals(result.get_absolute_url(), '/1/test')



