from django.contrib import admin

from categoriya.models import Category

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
