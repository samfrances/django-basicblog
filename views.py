from django.views.generic.dates import ArchiveIndexView, MonthArchiveView, DateDetailView, BaseDateListView
from django.shortcuts import get_object_or_404
from portfolio.blog.models import Post, Category
from portfolio.views import ExtraContextMixin 
from datetime import datetime
from django.http import Http404
from django.template.defaultfilters import slugify

class BlogBase(ExtraContextMixin):

    def get_extra_context(self):
        categories = Category.objects.all()
        months = Post.objects.all().dates(self.get_date_field(), 'month', order="DESC")
        try:
            extra_context = self.extra_context
        except AttributeError:
            extra_context = dict()
        extra_context['categories'] = categories
        extra_context['months'] = months
        extra_context['pagename'] = 'blog'
        return extra_context

class BlogHome(BlogBase, ArchiveIndexView):
    model = Post
    paginate_by = 10
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
    paginate_by = 10
    date_field = 'publication_date'
    month_format = '%m'
    context_object_name = 'posts'
    template_name = 'blog/home.html'

class CategoryBlogView(BlogHome):
    def get_queryset(self):
        tag = self.kwargs['tag']
        category = Category.objects.get(name=tag)
        queryset = category.post_set.all()
        return queryset
