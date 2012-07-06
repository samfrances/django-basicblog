"""RssFeed and AtomFeed views"""

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from portfolio.blog.models import Post
from datetime import tzinfo, timedelta

class RssFeed(Feed):
    title = "Sam Frances's blog"
    link = '/blog/'
    description = 'Blog updates from samfrances.co.uk'
   
    def items(self):
        return Post.objects.order_by('-publication_date')
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.body
    
    def item_pubdate(self, item):
        return item.publication_date

class AtomFeed(RssFeed):
    feed_type = Atom1Feed
    subtitle = RssFeed.description
