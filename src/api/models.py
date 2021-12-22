from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    source = models.URLField(max_length=255, null=True, blank=True)
    observed_authenticity = models.BooleanField(default=True)
    predicted_authenticity = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class FeedBack(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    authentic = models.BooleanField(default=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.article.title