from django.db import models
from django.urls import reverse

from mptt.fields import TreeForeignKey

from mptt.models import MPTTModel

# Maxsulot kategoriyasi
class ProductCategory(MPTTModel):
    name = models.CharField(max_length=124)
    description = models.TextField(null=True, blank=True)
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    
    slug = models.SlugField(null=False, unique=True)
    
    class MPTTMeta:
        order_insertion_by = ['name']


    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])



#Maxsulotlar
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='media/prod_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)


# Banner qo'shish
class Banner(models.Model):
    title = models.CharField(max_length=56, verbose_name="Banner Nomi ")
    image = models.ImageField(upload_to='images/banners/%Y/%m/%d',null=False, verbose_name="Rasm yuklang")

    def __str__(self):
        return self.title
    