from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'email', 'password', 'first_name', 'last_name', 'phone', 'email', 'role', 'image', 'is_active',
        'is_staff'
    )
    list_display_links = (
        'email',
    )
