from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def cartpage(request):
    return render(request, 'cart.html')


def productdtl(request):
    return render(request, 'productdtl.html')