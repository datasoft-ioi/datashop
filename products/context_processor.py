from .models import ProductCategory


def product_category_render(request):
    
    return {
        'categories': ProductCategory.objects.filter(parent=None)
    }
    