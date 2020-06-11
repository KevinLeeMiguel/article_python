from django.test import TestCase
from .models import Article


class TestModels(TestCase):

    def test_str(self):
        article = Article()
        article.title = 'hello'
        article.description = 'Description'
        expected_object_name = article.title
        self.assertEquals(expected_object_name, str(article))

        print('1. MODELS Testing toString article Passed!...')