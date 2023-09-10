from django.contrib import admin

from catalog.models import Category, Product, Blog


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name',)


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name', 'price', 'category',)
	list_filter = ('category',)
	search_fields = ('name', 'description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'image',)

