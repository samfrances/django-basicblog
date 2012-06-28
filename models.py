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
    publication_date = models.DateField(default=datetime.now)
    body = models.TextField()
    tags = models.ManyToManyField(Category)
    
    def save(self, *args, **kargs): # Modified save that sets the slug the first time the title is set
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kargs)    

    def __unicode__(self):
        return self.title
