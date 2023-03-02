from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),


    path('product/<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),


    # path('categoryList/', views.category_list) ,

    path('all_products/', views.all_products, name='all_products'),

    path('category/<int:id>/<slug:slug>/', views.category_products, name="category_products")

    
]
