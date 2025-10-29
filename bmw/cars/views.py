from django.shortcuts import render, get_object_or_404
from .models import Person
# Create your views here.

def cars(request):
    return render(request, 'cars.html')

def persons(request):
    persons = Person.objects.all()
    return render(request, 'persons.html', {'persons': persons})

def person_detail(request, slug):
    person = get_object_or_404(Person, slug=slug)
    return render(request, 'person_detail.html', {'person': person})