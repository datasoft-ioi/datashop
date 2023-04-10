from django.urls import path

from .views import ProductsListView, basket, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('savat/', basket, name='basket'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
