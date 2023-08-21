from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


#Code taken from CodeInstitute walktrough on a Django blog
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_data')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_data')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_data', 'approved')
    list_filter = ('approved', 'created_data')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)