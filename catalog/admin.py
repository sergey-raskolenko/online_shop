from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name',)


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name', 'price', 'category',)
	list_filter = ('category',)
	search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
	list_display = ('product', 'version_name', 'version_number', 'is_active',)
	list_filter = ('product',)
	search_fields = ('product', 'is_active',)

