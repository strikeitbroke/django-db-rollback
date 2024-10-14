from rest_framework import serializers
from .models import Author, Category, Comment
from blog.models import Article


# Author serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']


# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text']


# Article serializer
class ArticleSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)  # Nested Author serializer
    category = CategorySerializer()  # Nested Category serializer
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')  # Nested comments

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'authors', 'category', 'comments']
