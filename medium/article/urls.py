from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from article.views.article import ArticleView, ArticleDetailView
from article.views.author import AuthorView, AuthorDetailView
from article.views.login import LoginView

app_name = "articles"

urlpatterns = [
    path('articles', ArticleView.as_view()),
    path('articles/<int:pk>/', ArticleDetailView.as_view()),
    path('author', AuthorView.as_view()),
    path('author/<int:pk>/', AuthorDetailView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
