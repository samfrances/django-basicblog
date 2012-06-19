from django.views.generic.dates import ArchiveIndexView
from portfolio.blog.models import Post, Category
from portfolio.views import _BasicViewMixin

class BlogHome(_BasicViewMixin, ArchiveIndexView):
    queryset = Post.objects.all()
    paginate_by = 10
    date_field = 'publication_date'
    template_name = 'blog.html'
    context_object_name = 'posts'
    pagename = 'blog'
