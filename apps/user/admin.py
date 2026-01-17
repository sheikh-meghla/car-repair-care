from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomAdminClass(ModelAdmin):
    list_display = (
        'email',
        'role',
        'is_active',
        'is_staff',
    )

    list_filter = ('role', 'is_active')
    search_fields = ('email',)