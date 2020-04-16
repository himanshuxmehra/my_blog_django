from django.contrib import admin
from .models import Post,Comments


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'updated_on', 'status')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on', 'post')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']


admin.site.register(Post, PostAdmin)