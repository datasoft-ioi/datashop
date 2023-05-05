from django.db import models
from django.urls import reverse

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from users.models import User

# Maxsulot kategoriyasi
class ProductCategory(MPTTModel):
    name = models.CharField(max_length=124)
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    
    slug = models.SlugField(null=False, unique=True)
    
    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])


# Maxsulotlar
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='media/prod_images')
    category = models.ManyToManyField(to=ProductCategory)

    class Meta:
        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"

    
    def __str__(self) -> str:
        return self.name



# Banner qo'shish
class Banner(models.Model):
    title = models.CharField(max_length=56, verbose_name="Banner Nomi ")
    image = models.ImageField(upload_to='images/banners/%Y/%m/%d',null=False, verbose_name="Rasm yuklang")

    def __str__(self):
        return self.title
    

class TanlanganQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)
    

class BasketQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

# Savat 
class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()


    def __str__(self) -> str:
        return f"{self.user.username} uchun Savat | Maxsulot: {self.product.name}"
        
    def sum(self):
        return self.product.price * self.quantity


    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return basket_item

    @classmethod
    def create_or_update(cls, product_id, user):
        baskets = Basket.objects.filter(user=user, product_id=product_id)

        if not baskets.exists():
            obj = Basket.objects.create(user=user, product_id=product_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_crated = False
            return basket, is_crated


class Tanlangan(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = TanlanganQuerySet.as_manager()


    def __str__(self) -> str:
        return f"{self.user.username} uchun Savat | Maxsulot: {self.product.name}"
        
    def sum(self):
        return self.product.price * self.quantity
    

