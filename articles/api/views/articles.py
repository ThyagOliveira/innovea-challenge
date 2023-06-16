import requests, os
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from articles.models import Article
from articles.api.serializers.articles import ArticleSerializer


class ArticlesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


    @action(detail=False, methods=["POST"], url_path="load_articles")
    def load_articles(self, request):
        url = "https://newsapi.org/v2/top-headlines"

        params = {
            "country": "us",
            "apiKey": os.environ.get('API_KEY')
        }

        response = requests.get(url, params=params)
        articles_data = response.json()["articles"]
        
        articles_to_create = []

        for article_data in articles_data:
            article, created = Article.objects.get_or_create(
                author=article_data["author"],
                title=article_data["title"],
                description=article_data["description"]
            )
            
            if created:
                article.save()
        
        return Response(status=status.HTTP_200_OK)