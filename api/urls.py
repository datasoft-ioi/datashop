from django.conf.urls import url
from django.urls import path, include
from .views import (
    CategoryListApiView,
)

urlpatterns = [
    path('cateogry/', CategoryListApiView.as_view()),
]