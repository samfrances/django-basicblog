from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "categories"      # Corrects incorrect pluralisation of "category" in admin interface

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120)
    publication_date = models.DateField(default=datetime.now)
    body = models.TextField()
    tags = models.ManyToManyField(Category)
    
    def __unicode__(self):
        return self.title
