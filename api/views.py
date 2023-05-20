from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from products.models import ProductCategory,Product,Banner,Basket,Tanlangan
from .serializers import CategorySerializer,ProductSerializer,BannerSerializer,BasketSerializer,TanlanganSerializer
from rest_framework import status,generics
from .pagination import CustomPaagination


class CategoryListCreteAPIView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPaagination


class CategoryListAPIView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPaagination


class ProductListCreteAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPaagination


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPaagination


class BannerListCreteAPIView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    pagination_class = CustomPaagination


class BannerListAPIView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    pagination_class = CustomPaagination


class BasketListCreteAPIView(generics.ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    pagination_class = CustomPaagination


class BasketListAPIView(generics.ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    pagination_class = CustomPaagination




class TanlanganListCreteAPIView(generics.ListCreateAPIView):
    queryset = Tanlangan.objects.all()
    serializer_class = TanlanganSerializer
    pagination_class = CustomPaagination


class TanlanganListAPIView(generics.ListAPIView):
    queryset = Tanlangan.objects.all()
    serializer_class = TanlanganSerializer
    pagination_class = CustomPaagination

# class CategoryListApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         categoryies = ProductCategory.objects.all()
#         serializer = CategorySerializer(categoryies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def post(self, request, *args, **kwargs):
#         data = {
#             'name': request.data.get('name'), 
#             'parent': request.data.get('parent'),
#             'slug': request.data.get('slug'),
#         }
#         serializer = CategorySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
