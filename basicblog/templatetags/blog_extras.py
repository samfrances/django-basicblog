from django import template
from ..models import Post, Category
import re

register = template.Library()

@register.tag
def get_blog_vars(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
    m = re.search(r"as (\w+)", arg)
    if not m:
        raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
    var_name = m.groups()[0]
    return BlogVarsNode(var_name)

class BlogVarsNode(template.Node):
    
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        blog_vars = dict()
        blog_vars['months'] = Post.objects.all().dates('publication_date', 'month', order="DESC")
        blog_vars['categories'] = Category.objects.all()
        context[self.var_name] = blog_vars
        return ''
