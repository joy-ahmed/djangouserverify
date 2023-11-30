from django.contrib import admin

from base_app.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'first_name', 'last_name', 'date_joined', 'is_staff', 'is_superuser', 'is_active']