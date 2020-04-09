from django.contrib import admin
from .models import Items, ItemOrder, OrderPlaced

admin.site.register(OrderPlaced)
admin.site.register(ItemOrder)
admin.site.register(Items)
