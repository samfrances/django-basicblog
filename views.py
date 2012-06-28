from django.views.generic.dates import ArchiveIndexView, DateDetailView, BaseDateListView
from django.shortcuts import get_object_or_404
from portfolio.blog.models import Post, Category
from portfolio.views import _BasicViewMixin
from datetime import datetime
from django.http import Http404
from django.template.defaultfilters import slugify

class _MonthListMixin(object):
    def get_context_data(self, **kwargs):
        context = super(_MonthListMixin, self).get_context_data(**kwargs)
        context['months'] = self.get_queryset().dates(self.get_date_field(), 'month', order="DESC")
        return context

class BlogHome(_MonthListMixin, _BasicViewMixin, ArchiveIndexView):
    model = Post
    paginate_by = 10
    date_field = 'publication_date'
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    pagename = 'blog'

class SinglePost(_MonthListMixin, _BasicViewMixin, DateDetailView,):
    model = Post
    date_field = 'publication_date'
    month_format = '%m'
    pagename = 'blog'
    context_object_name = 'post'
    template_name = 'blog/singlepost.html'
