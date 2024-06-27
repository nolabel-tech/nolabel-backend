from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    # Поля, которые будут отображаться в списке пользователей
    list_display = ('email', 'username', 'unique', 'token', 'is_active', 'is_admin', 'is_superuser')
    list_filter = ('is_admin', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'unique', 'token')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'unique', 'password1', 'password2', 'is_active', 'is_admin', 'is_superuser')}
         ),
    )
    search_fields = ('email', 'username', 'unique')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
