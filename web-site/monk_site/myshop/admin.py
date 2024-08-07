from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Color, Product, Gender


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show']
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка цвета"


# class GalleryInline(admin.TabularInline):
#     fk_name = 'product'
#     model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show', 'price', 'available', 'created', 'uploaded']
    list_filter = ['available', 'created', 'uploaded']
    list_editable = ['price', 'available']
    # prepopulated_fields = {'slug': ('name',)}
    # inlines = [GalleryInline, ]

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"
