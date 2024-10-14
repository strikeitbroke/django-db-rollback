from rest_framework import generics
from .models import Author
from blog.models import Article
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleByAuthorView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        name = self.kwargs.get("name")
        author = get_object_or_404(Author, name=name)
        return author.authors_to_blog_article.all()
