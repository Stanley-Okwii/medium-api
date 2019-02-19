from django.urls import path

from article.views.article import ArticleView
from article.views.author import AuthorView

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('author/', AuthorView.as_view()),
]
