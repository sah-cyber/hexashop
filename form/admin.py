from django.contrib import admin
from . models import ContactForm,Contact


class FormAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = ('name', 'email','text', 'creted_at', 'creted_up')
    search_fields = ('name',)
    list_display_links = ('name',)
    # list_editable = ('public',)
    list_filter = ('name',)


admin.site.register(Contact,FormAdmin)

