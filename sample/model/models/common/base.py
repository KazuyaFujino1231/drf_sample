from django.db import models
from django.utils import timezone

class UpdateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 抽象基底クラスとしてされることを示す。
        # これにより、Djangoはこのモデルのためのデータベーステーブルを作成しない。
        abstract = True

class LogicalDeleteModel(UpdateModel):
    deleted_at = models.DateTimeField(null=True)

    def logical_delete(self):
        self.deleted_at = timezone.now()
        self.save(update_fields=['deleted_at'])

    class Meta:
        abstract = True