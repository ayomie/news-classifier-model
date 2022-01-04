from django.db import models


class Article(models.Model):
    title = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    source = models.URLField(max_length=255, null=True, blank=True)
    label = models.BooleanField(default=True)
    predicted_label = models.BooleanField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ('-created_at', )


class FeedBack(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    authentic = models.BooleanField(default=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.article.title

    class Meta:
        ordering = ('-created_at', )