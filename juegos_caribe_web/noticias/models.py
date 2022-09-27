import search_engine.loader as search_loader

from django.db import models
from django.utils.text import slugify
from django.conf import settings

class New(models.Model):
    title = models.CharField(max_length=50)
    published = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, default='Admin del sitio')
    slug = models.SlugField()
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    body = models.TextField()

    class Meta:
        ordering = ['-published']
    
    def __str__(self):
        return self.title

    def __lt__(self, other):
        return True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(New, self).save(*args, **kwargs)
        search_loader.load_models(New, 'title', 'body')
