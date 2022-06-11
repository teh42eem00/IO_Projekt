from django.db import models
from django.utils.text import slugify


class Car(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Car, self).save(*args, **kwargs)

    @property
    def budget_left(self):
        expense_list = Expense.objects.filter(car=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount += expense.amount

        return self.budget - total_expense_amount

    @property
    def total_transactions(self):
        expense_list = Expense.objects.filter(car=self)
        return len(expense_list)


class Expense(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(choices=(
        ('Service', "Service"),
        ('Fuel', "Fuel"),
        ('Expense', "Expense"),
    ),
        max_length=10
    )
    mileage = models.IntegerField(default=0)

    class Meta:
        ordering = ('-amount',)
