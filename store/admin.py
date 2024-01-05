from django.contrib import admin

from store.models import Product,Category,Basket

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Basket)
