from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def say_hello(request):
    # return HttpResponse('Hello, Django!')
    return render(request, 'say_hello.html', {'name': 'Bayizere Marius', 'age': 25})


def get_All_Products(request):
    products = Product.objects.all()
    for product in products:
        print(product)


def get_product(request, id):
    try:
        product = Product.objects.get(pk=id)
    except ObjectDoesNotExist:
        return HttpResponse('Product not found')
    return render(request, 'product.html', {'product': product})


def get_product(request, id):
    product = product.objects.filter(pk=id).exists()
    if not product:
        return HttpResponse('Product not found')
    return render(request, 'product.html', {'product': product})