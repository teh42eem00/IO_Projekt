from django.shortcuts import render, get_object_or_404
from .models import Car, Category
from django.views.generic import CreateView
from django.utils.text import slugify
from django.http import HttpResponseRedirect

# Create your views here.
def car_list(request):
    return render(request,'car_budget/car-list.html')

def car_detail(request,car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    expense_list = car.expenses
    return render(request,'car_budget/car-detail.html', {'car': car, 'expense_list' : car.expenses.all()})

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_budget/add-car.html'
    fields = ('name','budget')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
                car=Car.objects.get(id=self.object.id),
                name=category
            ).save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])
