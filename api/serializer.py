from django.db.models import fields
from rest_framework import serializers

from .models import *
from .utils import predict


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

    def create(self, validated_data):
        from .apps import ApiConfig
        text = validated_data.get("text")
        response = ApiConfig.predict(text)
        predicted = response[0]
        if predicted == 0:
            validated_data["predicted_label"] = False
        if predicted == 1:
            validated_data["predicted_label"] = True

        return super().create(validated_data)


class ArticleFeebackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = "__all__"