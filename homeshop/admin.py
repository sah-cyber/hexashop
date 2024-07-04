from django.contrib import admin

from categoriya.models import Category
from .models import Product
from django.utils.safestring import mark_safe

from .views import ContactForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','stock','author','status','publish','category','get_img_product','created','updated')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

    # class Meta:
    #     model = Category






    def get_img_product(self, object):
        return mark_safe(f"<img src = '{object.product_image.url}' width=70>")

    get_img_product.short_description = 'Product_img'

#
# @admin.register(ContactForm)
#
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'message')
#     search_fields = ('name', 'email', 'message')