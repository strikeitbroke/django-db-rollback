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

    def __str__(self):
        return self.name


# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"
    title = models.CharField(max_length=200)
    content = models.TextField()
    authors = models.ManyToManyField('quickstart.Author', related_name="authors_to_%(app_label)s_%(class)s")  # Many-to-Many with Author
    category = models.ForeignKey('quickstart.Category', related_name="category_to_%(app_label)s_%(class)s", on_delete=models.CASCADE)


# Comment model (One-to-Many relationship with Article)
class Comment(models.Model):
    class Meta:
        db_table = "comment"
    article = models.ForeignKey('quickstart.Article', on_delete=models.CASCADE)  # One-to-Many
    text = models.TextField()

