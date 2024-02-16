from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Category, Post, Comment

admin.site.register(CustomUser, UserAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_on', 'last_modified']
    list_max_show_all = 1
    search_fields = ['title', 'author']
    list_filter = ['created_on', 'last_modified', 'categories']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'post', 'created_on']
    search_fields = ['author__username', 'post__title']
    list_filter = ['created_on']
