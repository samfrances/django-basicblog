from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "categories"      # Corrects incorrect pluralisation of "category" in admin interface

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, blank=True, unique_for_date='publication_date')
    publication_date = models.DateTimeField(default=datetime.now)
    body = models.TextField()
    tags = models.ManyToManyField(Category)
    
    def __unicode__(self):
        return self.title
    
    @property
    def url(self):
        date = self.publication_date
        return "/blog/{0}/{1}/{2}/{3}/".format(date.year, date.month, date.day, self.slug)
