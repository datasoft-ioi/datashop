from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


from .models import Product, ProductCategory, Banner, Basket
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Aso'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['banner'] = Banner.objects.all().order_by('-id')[:10]
        context['product_noutbuklar'] = Product.objects.filter(category__parent=14)
        return context


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 1

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')

        return queryset.filter(category__id=category_id) if category_id else queryset



    def get_context_data(self, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context["title"] = "title"
        context['categories'] = ProductCategory.objects.filter(parent=None)
        return context



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

