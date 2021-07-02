from django.db import models

from account_app.models import Account


class Category(models.Model):
    category_name = models.CharField(max_length=125, unique=True)  # Сущность называтьеся категория, зачем добавлять в название атрибуту ее название, дублирование бесполезное
    time_create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, unique=True)
    description = models.TextField(blank=True)
    creator_post = models.ForeignKey('account_app.Account', related_name='posts', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
