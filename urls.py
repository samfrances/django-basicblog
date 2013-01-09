from django.conf.urls.defaults import patterns, include, url
from portfolio.blog.views import BlogHome, SinglePost, MonthBlogView, CategoryBlogView
from portfolio.blog.feeds import RssFeed, AtomFeed
from portfolio.blog.api.json.views import BlogHomeJson, SinglePostJson, CategoryBlogViewJson, MonthBlogViewJson

endings = r'^%s$'
json_endings = r'^%sjson/$'

monthpattern = r'(?P<year>\d{4})/(?P<month>\d{1,2})/'
singlepattern = r'(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[A-Za-z0-9_\-]+)/'
categorypattern = 'tag/(?P<tag>[A-Za-z0-9]+)/'

urlpatterns = patterns('',
    (endings % monthpattern, MonthBlogView.as_view()),
    (json_endings % monthpattern, MonthBlogViewJson.as_view()),
    # name urlpattern used because otherwise the generic view confuses the permalink decorator in the Post model
    url(endings % singlepattern, SinglePost.as_view(), name='single_post_url'),
    (json_endings % singlepattern, SinglePostJson.as_view()),
    (r'^$', BlogHome.as_view()),
    (json_endings % '', BlogHomeJson.as_view()),
    (endings % categorypattern, CategoryBlogView.as_view()),
    (json_endings % categorypattern, CategoryBlogViewJson.as_view()),
    (r'^feeds/rss/$', RssFeed()),
    (r'^feeds/atom/$', AtomFeed()), 
    (r'^comments/', include('django.contrib.comments.urls')),
)
