"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf.urls.static import static
from django.conf import settings

from products.views import IndexView, ProductsListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="home"),
    path("products/", include('products.urls', namespace='products')),
    path("users/", include('users.urls', namespace='users')),

    # vaqtinchalik
    path("test/", ProductsListView.as_view(), name="saqlanganlar"),
    path("shop/", ProductsListView.as_view(), name="shopcart"),
    path("login/", ProductsListView.as_view(), name="login"),
    # path("home/", products, name="home"),
    path("user_index/", ProductsListView.as_view(), name="user_index"),
    path("myorders/", ProductsListView.as_view(), name="myorders"),
    path("logout/", ProductsListView.as_view(), name="logout"),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
