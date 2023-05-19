from rest_framework import serializers
from products.models import ProductCategory


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ["name", "slug", "parent"]




