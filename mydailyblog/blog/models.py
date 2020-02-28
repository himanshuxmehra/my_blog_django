from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0,'Draft'),
    (1,'Published')
)  


class Post (models.Model):
    title = models.CharField(unique=True, max_length=200)
    slug = models.SlugField(unique=True,)
    tag = models.CharField(blank=False, default='ShitPost', max_length=25)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta():
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    