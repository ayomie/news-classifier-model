from django.db.models import fields
from rest_framework import serializers

from .models import *
import pickle

class ArticleFeebackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = "__all__"

    def to_representation(self, obj):
        self.fields['article'] = ArticleSerializer()
        return super().to_representation(obj)


class ArticleSerializer(serializers.ModelSerializer):
    # feedbacks = serializers.SerializerMethodField()
    feedbacks = ArticleFeebackSerializer(read_only=True)

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

    # def get_feedbacks(self, obj):
    #     return ArticleFeebackSerializer(obj.feedback_set.all(), many=True).data

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
