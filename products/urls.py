from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products, name='index'),
    path('category/<int:category_id>/', views.products, name='category'),
    path('page/<int:page>/', views.products, name='paginator'),
    path('savat/', views.basket, name='basket'),
    path('basket/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]
