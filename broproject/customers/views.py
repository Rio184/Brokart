from django.shortcuts import render

# Create your views here.
def customer_details(request):
    return render(request,'accounts.html')