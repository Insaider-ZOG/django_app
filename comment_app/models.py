from django.db import models

from account_app.models import Account
from post_app.models import Post


class Comment(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    creator_comment = models.ForeignKey('account_app.Account', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('post_app.Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'