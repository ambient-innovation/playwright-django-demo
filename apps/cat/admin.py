from django.contrib import admin

from cat.models import Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
