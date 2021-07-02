from django.contrib import admin

from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'time_update', 'is_published']
    list_filter = ['is_published']
    list_display_links = ['title']
    fieldsets = (
        ('title', {
            'fields': ('title', 'description', 'creator_post')
        }),
        ('Info', {
            'fields': ('is_published', 'category')
        }),
    )
    search_fields = ['creator_post']
    ordering = ['id', ]

    filter_horizontal = ()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
    list_display_links = ['category_name']
    search_fields = ['posts']
    ordering = ['id', ]

    filter_horizontal = ()