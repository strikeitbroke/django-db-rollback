from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Author model (Many Authors can write Many Articles)
class Author(models.Model):
    class Meta:
        db_table = "author"
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)


# Comment model (One-to-Many relationship with Article)
class Comment(models.Model):
    class Meta:
        db_table = "comment"
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE)  # One-to-Many
    text = models.TextField()

