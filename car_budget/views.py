from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView
from django.utils.text import slugify
from .models import Car, Expense
from .forms import ExpenseForm
import json


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_budget/car-list.html', {'car_list': cars})


def car_detail(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    category_list = ['Service', 'Fuel', 'Expense']
    if request.method == 'GET':
        return render(request, 'car_budget/car-detail.html',
                      {'car': car, 'expense_list': car.expenses.all(), 'category_list': category_list})

    elif request.method == 'POST':
        # process the form
        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category = form.cleaned_data['category']
            mileage = form.cleaned_data['mileage']

            Expense.objects.create(
                car=car,
                title=title,
                amount=amount,
                category=category,
                mileage=mileage
            ).save()

    elif request.method == 'DELETE':
        try:
            id = json.loads(request.body)['id']
            expense = Expense.objects.get(id=id)
            expense.delete()
        except:
            return HttpResponse(status=404)

        return HttpResponse(status=204)

    return HttpResponseRedirect(car_slug)


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_budget/add-car.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])
