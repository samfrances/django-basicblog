from django.contrib import admin
from portfolio.blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    fields = ('title', 'slug', 'publication_date', 'body', 'tags')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
