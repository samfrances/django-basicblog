from django.conf.urls.defaults import patterns, include, url
from portfolio.blog.views import BlogHome, SinglePost

urlpatterns = patterns('',
    (r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>.+)/$', SinglePost.as_view()),
    (r'^$', BlogHome.as_view()),
)
