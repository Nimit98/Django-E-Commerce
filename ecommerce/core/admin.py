from django.contrib import admin
from .models import Items, ItemOrder, UserList, OrderPlaced


class OrderPlacedInline(admin.TabularInline):
    model = OrderPlaced
    extra = 1


class UserAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['user']}), ]
    inlines = [OrderPlacedInline]


admin.site.register(UserList, UserAdmin)
admin.site.register(ItemOrder)
admin.site.register(Items)
