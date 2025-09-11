from rest_framework import serializers

from sample.model.models.tweet import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ("user", "content")

    def save(self, **kwargs):
        return super().save(**kwargs)
