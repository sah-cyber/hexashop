from django.contrib import admin
from about.models import About
# Register your models here.


@admin.register(About)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    prepopulated_fields = {'slug': ('name',)}