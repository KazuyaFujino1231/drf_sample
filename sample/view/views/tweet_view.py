from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from sample.model.models.tweet import Tweet
from sample.serializer.tweet_serializer import TweetSerializer

class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
