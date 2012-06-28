from django.contrib import admin
from portfolio.blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'publication_date', 'body', 'tags')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
