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
    path('tanlanganlar/', views.tanlangan, name='tanlanganlar'),
    path('tanlanganlar/add/<int:product_id>/', views.tanlangan_add, name='tanlangan_add'),
    path('tanlanganlar/remove/<int:tanlangan_id>/', views.tanlangan_remove, name='tanlangan_remove'),
    path('tanlanganlar/remove/all', views.tanlangan_remove_all, name='tanlangan_remove_all'),
]
