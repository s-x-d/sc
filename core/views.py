from django.shortcuts import render
from .models import Car

# Create your views here.
def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})
