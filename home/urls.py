from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('d', views.index, name="shopcart"),
    path('ddd', views.index, name="login"),
    path('dd', views.index, name="logout"),

    path('cart/', views.cartpage) ,

    path('product/<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),


    # path('categoryList/', views.category_list) ,
    path('register/', views.register) ,
    path('login/', views.login) ,
    path('korzinka/', views.korzinka),

    path('category/<int:id>/<slug:slug>/', views.category_products, name="category_products")
    
]
