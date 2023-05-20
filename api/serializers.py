from rest_framework import serializers
from products.models import ProductCategory,Product,Banner,Tanlangan,Basket


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ["name", "slug", "parent"]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["name", "description", "price", 'quantity','image', 'category']

class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = ["title", 'image']


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ["__all__"]

class TanlanganSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tanlangan
        fields = ["__all__"]
