from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'last_login',
        'date_joined',
    )
    list_filter = ('is_active', 'is_superuser', 'role')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('id',)


admin.site.register(User, UserAdmin)
