from django.db import models
from .user import User
from .common.base import LogicalDeleteModel  

class Tweet(LogicalDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets", verbose_name="ユーザー")
    content = models.CharField(max_length=280, verbose_name="内容")

    class Meta:
        db_table = "tweets"
        verbose_name = verbose_name_plural = "ツイート"