from django.test import SimpleTestCase
from car_budget.forms import ExpenseForm


class TestForms(SimpleTestCase):

    def test_expense_form_valid_data(self):
        form = ExpenseForm(data={
            'title': 'Oil Change',
            'amount': 1000,
            'mileage': 10000,
            'category': 'Service'
        })

        self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self):
        form = ExpenseForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
