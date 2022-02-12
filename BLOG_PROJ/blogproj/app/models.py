from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_author = models.CharField(max_length=70)
    post_title = models.CharField(max_length=100)
    # post_content = models.CharField(max_length=1000)
    post_content = RichTextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to="myimage", null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    body = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="+")

    @property
    def children(self):
        print("hello this is model running----------------------------------------------")
        return Comment.objects.filter(parent=self).order_by('-creation_date').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
