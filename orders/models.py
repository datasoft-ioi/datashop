from django.db import models

from products.models import Basket
from users.models import User

from django.db import models

# class Order(models.Model):
#     DELIVERY_METHOD_CHOICES = [
#         ('pickup', 'Самовывоз'),
#         ('delivery', 'Доставка'),
#     ]
#     PAYMENT_METHOD_CHOICES = [
#         ('click', 'Click'),
#         ('payme', 'Payme'),
#         ('cash', 'Наличными'),
#     ]
#     delivery_method = models.CharField(max_length=20, choices=DELIVERY_METHOD_CHOICES)
##     region = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     additional_phone_number = models.CharField(max_length=20, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3

    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    DELIVERY_METHOD_CHOICES = [
        ('pickup', 'Самовывоз'),
        ('delivery', 'Доставка'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('click', 'Click'),
        ('payme', 'Payme'),
        ('cash', 'Наличными'),
    ]

    delivery_method = models.CharField(max_length=20, choices=DELIVERY_METHOD_CHOICES)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)   
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20)
    additional_phone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}'

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.status = self.PAID
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum()),
        }
        baskets.delete()
        self.save()

