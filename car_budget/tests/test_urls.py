from django.test import SimpleTestCase
from django.urls import reverse, resolve
from car_budget.views import car_list, car_detail, CarCreateView


class TestUrls(SimpleTestCase):
    def test_list_resolving(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, car_list)

    def test_car_create_resolving(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, CarCreateView)

    def test_car_detail_resolving(self):
        url = reverse('detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, car_detail)
