from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created', 'updated', 'published')
    list_editable = ('published',)
    list_display_links = ('title',)
    list_filter = ('published',)
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at')
    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
