from django.test import TestCase
from car_budget.models import Car, Expense


class TestModels(TestCase):

    def setUp(self) -> None:
        self.car1 = Car.objects.create(
            name='Car 1',
            budget=10000
        )
        self.car2 = Car.objects.create(
            name='Car 2',
            budget=10000
        )

    def test_car1_is_assigned_slug_on_creation(self):
        self.assertEquals(self.car1.slug, 'car-1')

    def test_budget_left(self):
        Expense.objects.create(
            car=self.car1,
            title='Oil Change',
            amount=1000,
            mileage=10000,
            category='Service'
        )
        Expense.objects.create(
            car=self.car1,
            title='Oil Change',
            amount=1000,
            mileage=11000,
            category='Service'
        )

        self.assertEquals(self.car1.budget_left, 8000)

    def test_project_total_transactions(self):

        Expense.objects.create(
            car=self.car2,
            title='Oil Change',
            amount=1000,
            mileage=11000,
            category='Service'
        )
        Expense.objects.create(
            car=self.car2,
            title='Oil Change',
            amount=1000,
            mileage=11000,
            category='Service'
        )
        self.assertEquals(self.car2.total_transactions, 2)
