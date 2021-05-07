from django.contrib import admin

from main.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name_uz',
        'name_ru'
    ]

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)