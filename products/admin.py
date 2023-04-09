from django.contrib import admin
from django.utils.html import format_html


from mptt.admin import DraggableMPTTAdmin

from .models import Product, ProductCategory, Banner, Basket


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "get_categories", "display_image")
    fields = ("image", "name", "description", ("price", "quantity"), "category")
    search_fields = ("name", )
    ordering = ("name", )


    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])
    
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))

    get_categories.short_description = "Categories"
    display_image.short_description = 'Image'


@admin.register(ProductCategory)
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('name',)}
    # inlines = [CategoryLangInline]
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = ProductCategory.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)


        # Add non cumulative product count
        qs = ProductCategory.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs


    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'


    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


# @admin.register(Basket)
class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0


admin.site.register(Banner)

