from django.contrib import admin

from sosialmedia.models import SosialMedia


@admin.register(SosialMedia)

class SosialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','url_inst','url_face','url_teleq','created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
