from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post, Group, Follow)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author", "group")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    list_editable = ("group",)
    empty_value_display = "-empty-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "created", "author", "post")
    search_fields = ("text",)
    list_filter = ("created",)
