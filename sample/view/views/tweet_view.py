from rest_framework.viewsets import ModelViewSet

from sample.model.models.tweet import Tweet
from sample.serializer.tweet_serializer import TweetSerializer


class TweetViewSet(ModelViewSet):
    """
    デフォルトアクションのお勉強用。
    DRFによって自動的に提供される。車輪の再開発が起こりやすいポイントなので要注意。
    """

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
