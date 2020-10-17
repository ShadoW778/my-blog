from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'created_date')
    list_display_links = ('author', 'title')
    search_fields = ('author', 'title', 'text', )


admin.site.register(Post, PostAdmin)