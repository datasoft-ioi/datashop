from django.contrib import admin

from .models import User, Profile

from products.admin import BasketAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ('username', )
   inlines = (BasketAdmin, )
   


admin.site.register(Profile)