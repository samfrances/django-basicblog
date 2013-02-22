from django.http import HttpResponse
from django.utils import simplejson
from django.contrib.comments.models import Comment
from basicblog.views import BlogHome, SinglePost, MonthBlogView, CategoryBlogView



class JsonMixin(object):
    response_class = HttpResponse
    paginate_by = None
    
    def prepare_data(self, data):
        return [self.blogpost_to_dict(post) for post in data]
    
    @classmethod
    def blogpost_to_dict(cls, post):
        
        comments = Comment.objects.filter(object_pk=post.pk).filter(is_public=True).filter(is_removed=False)
        comments = [cls.comment_to_dict(c) for c in comments]
        
        return {'title': post.title,
                'body': post.body,
                'publication_date': str(post.publication_date),
                'tags':[tag.name for tag in post.tags.all()],
                'comments': comments}
    
    @staticmethod
    def comment_to_dict(comment):
        return {'user_name': comment.user_name,
                'user_email': comment.user_email,
                'user_url': comment.user_url,
                'comment': comment.comment}
    
    def render_to_response(self, context, **response_kwargs):
        data = context[self.context_object_name]
        data = self.prepare_data(data)
        json_data = simplejson.dumps(data)
        return self.response_class(json_data, mimetype="application/json")

class BlogHomeJson(JsonMixin, BlogHome): pass

class MonthBlogViewJson(JsonMixin, MonthBlogView): pass

class CategoryBlogViewJson(JsonMixin, CategoryBlogView): pass

class SinglePostJson(JsonMixin, SinglePost):
    def prepare_data(self, data):
        return self.blogpost_to_dict(data)
