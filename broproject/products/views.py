from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def list_products(request):
    """_summery_
    returns product list page
    """
    return render(request,'products.html')

def products_details(request):
    return render(request,'product_details.html')


