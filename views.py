from django.views.generic.dates import ArchiveIndexView, DateDetailView
from django.shortcuts import get_object_or_404
from portfolio.blog.models import Post, Category
from portfolio.views import _BasicViewMixin
from datetime import datetime
from django.http import Http404
from django.template.defaultfilters import slugify

class BlogHome(_BasicViewMixin, ArchiveIndexView):
    queryset = Post.objects.all()
    paginate_by = 10
    date_field = 'publication_date'
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    pagename = 'blog'

class SinglePost(_BasicViewMixin, DateDetailView):
    def get_object(self, queryset=None):
        year, month, day = self.get_year(), self.get_month(), self.get_day() 
        year, month, day = int(year), int(month), int(day)
        slug = self.kwargs['slug']
        pk = int(self.kwargs['pk'])
        ob = get_object_or_404(Post, publication_date=datetime(year, month, day), slug__exact=slug, id=pk)
        return ob
    date_field = 'publication_date'
    month_format = '%m'
    pagename = 'blog'
    context_object_name = 'post'
    template_name = 'blog/singlepost.html'
