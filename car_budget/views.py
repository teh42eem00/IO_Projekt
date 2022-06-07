from django.shortcuts import render, get_object_or_404
from .models import Car

# Create your views here.
def car_list(request):
    return render(request,'car_budget/car-list.html')

def car_detail(request,car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    expense_list = car.expenses
    return render(request,'car_budget/car-detail.html', {'car': car, 'expense_list' : car.expenses.all()})
