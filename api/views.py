from django.core import paginator
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .models import Article, FeedBack
from .serializer import ArticleSerializer, ArticleFeebackSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = PageNumberPagination


class ArticleFeedbackViewSet(ModelViewSet):
    queryset = FeedBack.objects.all()
    serializer_class = ArticleFeebackSerializer
    pagination_class = PageNumberPagination