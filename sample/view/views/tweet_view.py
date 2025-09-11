from rest_framework.viewsets import ModelViewSet

from sample.model.models.tweet import Tweet
from sample.serializer.tweet_serializer import TweetSerializer


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
