from django.conf.urls.defaults import patterns, include, url
from portfolio.blog.views import BlogHome, SinglePost, MonthBlogView, CategoryBlogView
from portfolio.blog.feeds import RssFeed, AtomFeed

urlpatterns = patterns('',
    (r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', MonthBlogView.as_view()),
    # name urlpattern used because otherwise the generic view confuses the permalink decorator in the Post model
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>.+)/$', SinglePost.as_view(), name='single_post_url'),
    (r'^$', BlogHome.as_view()),
    (r'^tag/(?P<tag>[A-Za-z]+)/$', CategoryBlogView.as_view()),
    (r'^feeds/rss/$', RssFeed()),
    (r'^feeds/atom/$', AtomFeed()), 
    (r'^comments/', include('django.contrib.comments.urls')),
)
