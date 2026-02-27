from django.db import models
from django.contrib.auth.models import User

class BlogCustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-id')
    
    def blog_count(self, keyword):
        return self.filter(name__icontains=keyword).count()

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='blog_images/')
    desc = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = BlogCustomManager()



