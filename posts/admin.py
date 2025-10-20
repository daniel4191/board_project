from django.contrib import admin

from .models import Post, Comment, PostImage

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "id",
        "content"
    ]
    
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo"
    ]
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content"
    ]