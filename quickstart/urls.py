from django.urls import path
from .views import ArticleListView, ArticleByAuthorView


urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/author/<str:name>/', ArticleByAuthorView.as_view(), name='article-by-author-name'),
]
