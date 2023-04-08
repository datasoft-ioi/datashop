from django.shortcuts import render

from .models import Product, ProductCategory, Banner, Basket


def index(request):


    context = {
        "banner": Banner.objects.all().order_by('-id')[:10],
        "product_by_category": Product.objects.filter(category__name="Noutbuk")
    }

    return render(request, 'products/index.html', context)


def products(request):
    context = {
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
    }

    return render(request, 'products/products.html', context)


def basket(request):


    context = {
        "basket": Basket.objects.all(),
    }

    return render(request, 'products/basket.html', context)
