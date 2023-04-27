from django.contrib import admin

from .models import User, Profile

from products.admin import BasketAdmin, TanlanganAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ('username', )
   inlines = (BasketAdmin, TanlanganAdmin)
   


admin.site.register(Profile)