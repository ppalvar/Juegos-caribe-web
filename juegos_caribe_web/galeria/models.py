from django.db import models
from django.conf import settings

class Image(models.Model):
    description = models.CharField(max_length=100, null=False)
    alt = models.CharField(max_length=20, null=False)
    added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)

    class Meta:
        ordering = ['-added']
    
    def __str__(self):
        return self.description
