from django.test import TestCase, Client
from django.urls import reverse
from car_budget.models import Car, Expense
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['car1'])
        self.car1 = Car.objects.create(
            name='car1',
            budget=10000
        )

    def test_car_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_budget/car-list.html')

    def test_car_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_budget/car-detail.html')

    def test_car_detail_POST_adds_new_expense(self):
        response = self.client.post(self.detail_url, {
            'title': 'Oil Change',
            'amount': 1000,
            'mileage': 10000,
            'category': 'Service'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.car1.expenses.first().title, 'Oil Change')

    def test_car_detail_POST_no_data(self):
        response = self.client.post(self.detail_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.car1.expenses.count(), 0)

    def test_car_detail_DELETE_deletes_expense(self):
        expense = Expense.objects.create(
            car=self.car1,
            title='Oil Change',
            amount=1000,
            mileage=10000,
            category='Service'
        )

        response = self.client.delete(self.detail_url, json.dumps({
            'id': expense.id
        }))
        self.assertEquals(response.status_code, 204)
        self.assertEquals(self.car1.expenses.count(), 0)

    def test_car_detail_DELETE_without_id(self):
        Expense.objects.create(
            car=self.car1,
            title='Oil Change',
            amount=1000,
            mileage=10000,
            category='Service'
        )

        response = self.client.delete(self.detail_url)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(self.car1.expenses.count(), 1)

    def test_car_create_POST(self):
        url = reverse('add')
        response = self.client.post(url, {
            'name': 'car2',
            'budget': 777,
        })

        car2 = Car.objects.get(slug='car2')
        self.assertEquals(car2.name, 'car2')
        self.assertEquals(car2.budget, 777)
