from django.db import models
from django_tidb.fields import BigAutoRandomField

# Create your models here.
class Post(models.Model):
    id = BigAutoRandomField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post: {self.title}"
    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    id = BigAutoRandomField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        tidb_auto_id_cache = 1

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        tidb_auto_id_cache = 1

from django_tidb.fields import BigAutoRandomField
class MyModel(models.Model):
    id = BigAutoRandomField(primary_key=True)
    title = models.CharField(max_length=200)