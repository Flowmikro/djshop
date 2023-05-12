from django.test import TestCase

from .models import Order


class OrderModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Order.objects.create(first_name='test',
                             last_name='test',
                             address='test',
                             city='test',
                             braintree_id='test',
                             )

    def test_order_first_name(self):
        result = Order.objects.get(id=1)
        field_label = result._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_order_first_name_max_length(self):
        result = Order.objects.get(id=1)
        field_label = result._meta.get_field('first_name').max_length
        self.assertEquals(field_label, 50)

    def test_order_last_name(self):
        result = Order.objects.get(id=1)
        field_label = result._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'Фамилия')

    def test_order_last_name_max_length(self):
        result = Order.objects.get(id=1)
        field_label = result._meta.get_field('first_name').max_length
        self.assertEquals(field_label, 50)

    def test_order_address(self):
        result = Order.objects.get(id=1)
        field_label = result._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'Адрес')

    def test_order_address_max_length(self):
        result = Order.objects.get(id=1)
        field_label = result._meta.get_field('address').max_length
        self.assertEquals(field_label, 250)

    def test_order_city(self):
        result = Order.objects.get(id=1)
        field_label = result._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'Город')

    def test_order_city_max_length(self):
        result = Order.objects.get(id=1)
        field_label = result._meta.get_field('city').max_length
        self.assertEquals(field_label, 100)

    def test_order_braintree_id(self):
        result = Order.objects.get(id=1)
        field_label = result._meta.get_field('braintree_id').verbose_name
        self.assertEquals(field_label, 'braintree id')

    def test_order_braintree_id_max_length(self):
        result = Order.objects.get(id=1)
        field_label = result._meta.get_field('braintree_id').max_length
        self.assertEquals(field_label, 150)








