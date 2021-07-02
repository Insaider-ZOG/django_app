from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'creator_comment', 'time_create', 'time_update', 'post']
    list_filter = ['creator_comment']
    list_display_links = ['creator_comment']
    fieldsets = (
        ('title', {
            'fields': ('description', )
        }),
        ('Info', {
            'fields': ('creator_comment', 'post')
        }),
    )
    search_fields = ['creator_post']
    ordering = ['id', ]

    filter_horizontal = ()