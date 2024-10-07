from django.db import models
from users.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=timezone.now)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='folioapp/media/blog')

    def __str__(self):
        return self.title

    def get_summary(self):
        return f'{ self.content[:300] }...' if len(self.content) > 100 else self.content


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return f"commented by {self.author} on {self.post}"
