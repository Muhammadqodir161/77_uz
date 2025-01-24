from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'full_name', 'role', 'is_staff', 'is_active')
    search_fields = ('phone_number', 'full_name')
    list_filter = ('role', 'is_active', 'is_staff')
    ordering = ('full_name',)
admin.site.register(Address)