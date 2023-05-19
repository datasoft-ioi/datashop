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
from django.views.static import serve

from products.views import index, products

from api import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("products/", include('products.urls', namespace='products')),
    path("users/", include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(urls)),

    # vaqtinchalik
    path("test/", products, name="saqlanganlar"),
    path("shop/", products, name="shopcart"),
    path("login/", products, name="login"),
    # path("home/", products, name="home"),
    path("user_index/", products, name="user_index"),
    path("myorders/", products, name="myorders"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]
urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), ]


