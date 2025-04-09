from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

# Create your views here.
# in django we have two class HttpResponse and HttpRequest
# in class of djngo class we use "HttpResponse" or "HttpRequest" to return the response 
# but there is the on used by rest framework which is having powerful features because is having swagger and used every time in Industry "that where we use  API_view()"

def product_list(request):
    return HttpResponse('this Marius Bayizere he is Djngo developer Now')

@api_view(['GET', 'PUT'])
def product_list(request, id):
        product = get_object_or_404(Product, pk=id)
        if request.method == 'GET':
             serializer = ProductSerializer(product)
             return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# SECOND WAY TO GET THE PRODUCT WITH TRY AND CATCH
# @api_view()
# def product_list(request, id):
#     try:
#         product = Product.objects.get(pk=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def product_lists(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)