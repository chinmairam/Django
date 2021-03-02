from django.contrib import admin
from .models import Product

# Register your models here.


# Admin registration
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'qty')    # Lists to display in admin
    list_filter = ('product_id',)         # On what basis filtering
    ordering = ('-qty',)                  # On what basis ordering
    search_fields = ('product_name',)     # For Searching name in admin
