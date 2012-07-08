from django.views.generic.dates import ArchiveIndexView, MonthArchiveView, DateDetailView, BaseDateListView
from django.shortcuts import get_object_or_404
from portfolio.blog.models import Post, Category
from datetime import datetime
from django.http import Http404
from django.template.defaultfilters import slugify

class BlogBase(object):
    """Base class for blog posts."""
    model = Post
    paginate_by = 5
    date_field = 'publication_date'
    context_object_name = 'posts'

class BlogHome(BlogBase, ArchiveIndexView):
    template_name = 'blog/home.html'

class SinglePost(BlogBase, DateDetailView,):
    month_format = '%m'
    context_object_name = 'post'
    template_name = 'blog/singlepost.html'

class MonthBlogView(BlogBase, MonthArchiveView):
    month_format = '%m'
    template_name = 'blog/month_archive.html'
    
    def get_queryset(self):
        """Override get_queryset method of MonthArchiveView (which by default displays posts in chronological order) to
        display posts in reverse chronological order (i.e. most recent to least recent)"""
        queryset = super(MonthBlogView, self).get_queryset().order_by('-publication_date')
        return queryset


class CategoryBlogView(BlogHome):
    template_name = 'blog/category_archive.html'
    
    def get_queryset(self):
        tag = self.kwargs['tag']
        category = Category.objects.get(name=tag)
        queryset = category.post_set.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(CategoryBlogView, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['tag']
        return context
