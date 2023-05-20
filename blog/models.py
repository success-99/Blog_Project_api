from django.db import models
from django.urls import reverse


# class Book(models.Model):
#     author = models.ForeignKey(
#         'auth.User',
#         on_delete=models.CASCADE
#     )
#     name = models.CharField(max_length=100)
#     isbn = models.IntegerField(max_length=16)
#     description = models.TextField()


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])
