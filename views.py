from django.views.generic.dates import ArchiveIndexView
from portfolio.blog.models import Post, Category

class BlogHome(ArchiveIndexView):
    queryset = Post.objects.all()
    paginate_by = 10
    date_field = 'publication_date'
    template_name = 'blog.html'
    context_object_name = 'posts'
    pagename = 'blog'

    def get_context_data(self, **kwargs):
        context = super(BlogHome, self).get_context_data(**kwargs)
        context['pagename'] = self.pagename
        return context
