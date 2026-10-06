from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_options = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort in sort_options:
        phones = phones.order_by(sort_options[sort])
    return render(request, 'catalog.html', {'phones': phones})


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'product.html', {'phone': phone})