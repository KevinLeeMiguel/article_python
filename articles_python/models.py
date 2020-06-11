from django.db import models


class Article(models.Model):
    title = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title 
