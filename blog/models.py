from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "blog_article"
    title = models.CharField(max_length=200)
    content = models.TextField()
    authors = models.ManyToManyField('quickstart.Author', related_name="authors_to_%(app_label)s_%(class)s")  # Many-to-Many with Author
    category = models.ForeignKey('quickstart.Category', related_name="category_to_%(app_label)s_%(class)s", on_delete=models.CASCADE)
