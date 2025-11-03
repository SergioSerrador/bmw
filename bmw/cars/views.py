from django.shortcuts import redirect, render, get_object_or_404
from .models import Person, Product
from django.contrib.auth.decorators import login_required
from .forms import UploadProduct

def cars(request):
    return render(request, 'cars.html')

def persons(request):
    persons = Person.objects.all()
    return render(request, 'persons.html', {'persons': persons})

def person_detail(request, slug):
    person = get_object_or_404(Person, slug=slug)
    return render(request, 'person_detail.html', {'person': person})

def list_products(request):
    return render(request, 'list.html')

@login_required(login_url='/users/login/')
def product_list_view(request):
    product_list = Product.objects.all()[:20]
    
    if request.method == 'POST':
        form = UploadProduct(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('cars:list_products')
    else:
        form = UploadProduct()
    return render(request, 'list.html', {'products': product_list, 'form': form})