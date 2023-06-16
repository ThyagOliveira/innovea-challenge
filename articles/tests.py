from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from articles.models import Article


class ArticlesViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_load_articles(self):
        url = reverse("api:article-load-articles")

        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        articles = Article.objects.all()
        self.assertGreater(len(articles), 0)

    def test_list_articles(self):
        Article.objects.create(author='Author 1', title='Title 1', description='Description 1')
        Article.objects.create(author='Author 2', title='Title 2', description='Description 2')

        url = reverse("api:article-list")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        articles = response.json()
        self.assertEqual(len(articles), 2)
        self.assertEqual(articles[0]['author'], 'Author 1')
        self.assertEqual(articles[1]['title'], 'Title 2')
