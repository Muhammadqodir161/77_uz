from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'seller', 'price', 'currency')
    search_fields = ('name', 'seller__full_name')  # Seller nomi orqali qidirish
    list_filter = ('category', 'status', 'currency')
    ordering = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
