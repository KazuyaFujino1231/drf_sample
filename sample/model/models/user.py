from django.db import models

from .common.base import UpdateModel


class User(UpdateModel):
    class Meta:
        db_table = "users"
        verbose_name = verbose_name_plural = "ユーザー"

    name = models.CharField(max_length=100, verbose_name="名前")
    birthday = models.DateField(verbose_name="生年月日")
    email = models.EmailField(unique=True, verbose_name="メールアドレス")
    phone_number = models.IntegerField(verbose_name="電話番号", null=True)
