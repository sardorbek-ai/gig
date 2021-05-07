from django.contrib import admin

from client.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'date_joined',
    ]

    class Meta:
        model = User

admin.site.register(User, UserAdmin)
