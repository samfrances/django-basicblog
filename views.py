from django.views.generic.dates import ArchiveIndexView, DateDetailView
from django.shortcuts import get_object_or_404
from portfolio.blog.models import Post, Category
from portfolio.views import _BasicViewMixin
from datetime import datetime
from django.http import Http404
from django.template.defaultfilters import slugify

class BlogHome(_BasicViewMixin, ArchiveIndexView):
    model = Post
    paginate_by = 10
    date_field = 'publication_date'
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    pagename = 'blog'

class SinglePost(_BasicViewMixin, DateDetailView):
    model = Post
    date_field = 'publication_date'
    month_format = '%m'
    pagename = 'blog'
    context_object_name = 'post'
    template_name = 'blog/singlepost.html'
