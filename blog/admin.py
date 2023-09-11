from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'image', 'slug', 'creation_date', 'is_published', 'views_count',)
