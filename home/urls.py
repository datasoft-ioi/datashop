from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('cart/', views.cartpage) ,
    path('detail/', views.productdtl),
    path('categoryList/', views.category_list)
]