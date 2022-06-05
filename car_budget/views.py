from django.shortcuts import render

# Create your views here.
def car_list(request):
    return render(request,'car_budget/car-list.html')

def car_detail(request,car_slug):
    return render(request,'car_budget/car-detail.html')
