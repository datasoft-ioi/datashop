"""datashop URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns

from user import views as UserViews
from order import views as OrderViews

from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name="home"),
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls'), name='user'),

    path('shopcart/', OrderViews.shopcart, name='shopcart'),

    path('login/', UserViews.login_form, name='login'),
    path('logout/', UserViews.logout_func, name='logout'),
    path('signup/', UserViews.signup_form, name='signup'),
    # path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
