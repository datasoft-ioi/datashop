from django.conf.urls import url
from django.urls import path, include
from .views import (
    CategoryListCreteAPIView,
    CategoryListAPIView,
    ProductListCreteAPIView,
    ProductListAPIView,
    BannerListCreteAPIView,
    BannerListAPIView,
    BasketListCreteAPIView,
    BasketListAPIView,
    TanlanganListCreteAPIView,
    TanlanganListAPIView,
)

urlpatterns = [
    path('cateogry/', CategoryListCreteAPIView.as_view()),
    path('cateogrylist/', CategoryListAPIView.as_view()),
    path('produc/', ProductListCreteAPIView.as_view()),
    path('produclist/', ProductListAPIView.as_view()),
    path('banner/', BannerListCreteAPIView.as_view()),
    path('bannerlist/', BannerListAPIView.as_view()),    
    path('basket/', BasketListCreteAPIView.as_view()),
    path('basketlist/', BasketListAPIView.as_view()),
    path('tanlangan/', TanlanganListCreteAPIView.as_view()),
    path('tanlanganlist/', TanlanganListAPIView.as_view()),
]