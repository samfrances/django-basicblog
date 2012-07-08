from django import template
from portfolio.blog.models import Post, Category

register = template.Library()

@register.tag
def get_blog_vars(parser, token):
    args = token.contents.split()
    if len(args) > 1:
        raise template.TemplateSyntaxError("%r tag does not take any arguments" % args[0])
    return BlogVarsNode()

class BlogVarsNode(template.Node):
    def render(self, context):
        context['blog'] = dict()
        context['blog']['months'] = Post.objects.all().dates('publication_date', 'month', order="DESC")
        context['blog']['categories'] = Category.objects.all()
        return ''
