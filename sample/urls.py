from django.conf import settings
from django.contrib import admin
from django.urls import path

from . import schema
from .view import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user", views.UserViewSet.as_view({"get": "list", "post": "create"})),
    path("tweet", views.TweetViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "tweet/<int:tweet_id>",
        views.TweetViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
]

if settings.DEBUG:
    # drf_spectacular 対応
    urlpatterns.extend(
        [
            # OpenAPI形式のAPIドキュメントがダウンロードできるエンドポイント
            path("schema/", schema.SchemaView.as_view(), name="schema"),
            # Swagger UIでAPIドキュメントを表示するエンドポイント
            path("docs/", schema.SwaggerView.as_view(), name="docs"),
            # RedocでAPIドキュメントを表示するエンドポイント
            path("redoc/", schema.RedocView.as_view(), name="redoc"),
        ]
    )
