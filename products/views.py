from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Product, ProductCategory, Banner, Basket


def index(request):

    context = {
        "banner": Banner.objects.all().order_by('-id')[:10],
        "product_noutbuklar": Product.objects.filter(category__parent=14)
    }

    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):

    products = Product.objects.filter(category__id=category_id) if category_id else Product.objects.all()

    per_page = 1
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page)

    context = {
        "categories": ProductCategory.objects.filter(parent=None),
        "products": products_paginator,

    }

    return render(request, 'products/products.html', context)


def basket(request):

    baskets = Basket.objects.filter(user=request.user)
    context = {
        "baskets": baskets,
        "total_sum": sum(basket.sum() for basket in baskets),
        "total_quantity": sum(basket.quantity for basket in baskets),
    }

    return render(request, 'products/basket.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

