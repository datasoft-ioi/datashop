from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cart/', views.cartpage) ,
    path('detail/', views.productdtl),

    path('categoryList/', views.category_list) ,
    path('register/', views.register) ,
    path('login/', views.login) ,
    path('korzinka/', views.korzinka),
    path('categoryList/', views.category_list)

]