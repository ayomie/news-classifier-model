from django.db.models import fields
from rest_framework import serializers

from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        extra_kwargs = {
            "title": {
                "required": True
            },
            "text": {
                "required": True
            },
            "source": {
                "required": True
            },
            "label": {
                "required": True
            },
            "predicted_label": {
                "read_only": True
            }
        }


class ArticleFeebackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = "__all__"