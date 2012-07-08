from django import template
from blog.models import Post, Category

register = template.Library()

def get_blog_vars(parser, token):
    args = token.contents.split()
    if len(args) > 1: except ValueError:
        raise template.TemplateSyntaxError("%r tag does not take any arguments" % args[0])
    return BlogVarsNode()

class BlogVarsNode(template.Node):
    def __init__(self):
        self.vars = dict()
        self.vars["categories"] = Category.objects.all()
        self.vars["months"] = Post.objects.all().dates(self.get_date_field(), 'month', order="DESC")
    def render(self, context):
        context['blog'] = self.vars
        return ''
