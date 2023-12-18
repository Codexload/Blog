from django.contrib import admin
from .models import Category, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
    search_fields = ('tiitle',)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('tiitle',)
    list_filter = ('cat',)
    list_per_page = 5
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js' ,'js/script.js',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'email', 'active')
    date_hierarchy = 'created'
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)