from django.db import models
from django.contrib.auth import get_user_model


class Posts(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=20)
    subject = models.TextField()
    date_post = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment

