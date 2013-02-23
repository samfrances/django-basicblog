from django.db import models
from datetime import datetime
from django.contrib.comments.moderation import CommentModerator, moderator

class Category(models.Model):
    name = models.SlugField(max_length=20, unique=True)
    
    class Meta:
        verbose_name_plural = "categories"      # Corrects incorrect pluralisation of "category" in admin interface

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique_for_date='publication_date')
    publication_date = models.DateTimeField(default=datetime.now)
    body = models.TextField()
    tags = models.ManyToManyField(Category)
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        """Calculates absolute url (doesn't include domain), with permalink decorator locating the relevant named
        urlpattern"""
        date = self.publication_date
        return ('single_post_url', (), { 'slug': self.slug, 'year': date.year, 'month': date.month, 'day': date.day })

class PostModerator(CommentModerator):
    email_notification = True

moderator.register(Post, PostModerator)
