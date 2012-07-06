from django.views.generic.dates import ArchiveIndexView, MonthArchiveView, DateDetailView, BaseDateListView
from django.shortcuts import get_object_or_404
from portfolio.blog.models import Post, Category
from portfolio.views import ExtraContextMixin 
from datetime import datetime
from django.http import Http404
from django.template.defaultfilters import slugify

class BlogBase(ExtraContextMixin):
    """Base class for blog posts. Provides the functionality of ExtraContextMixin and augments the context with a list
    of all blog post categories, all months for which there are blog articles, and other items"""
 

    paginate_by = 5

    def get_extra_context(self):
        categories = Category.objects.all()
        months = Post.objects.all().dates(self.get_date_field(), 'month', order="DESC")
        try:
            extra_context = self.extra_context
        except AttributeError:
            extra_context = dict()
        extra_context['categories'] = categories
        extra_context['months'] = months
        extra_context['current_tab'] = 'blog'
        return extra_context

class BlogHome(BlogBase, ArchiveIndexView):
    model = Post
    date_field = 'publication_date'
    template_name = 'blog/home.html'
    context_object_name = 'posts'

class SinglePost(BlogBase, DateDetailView,):
    model = Post
    date_field = 'publication_date'
    month_format = '%m'
    context_object_name = 'post'
    template_name = 'blog/singlepost.html'

class MonthBlogView(BlogBase, MonthArchiveView):
    model = Post
    date_field = 'publication_date'
    month_format = '%m'
    context_object_name = 'posts'
    template_name = 'blog/month_archive.html'

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
