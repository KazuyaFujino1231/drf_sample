from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


class SchemaView(SpectacularAPIView):
    custom_settings = {
        "TITLE": "DRF勉強会用サンプルAPI",
        "DESCRIPTION": "DRF勉強会用サンプルAPIのドキュメントです。",
        "TAGS": [
            {"name": "user", "description": "ユーザー管理API"},
            {"name": "tweet", "description": "ツイート管理API"},
        ],
    }
    urlconf = ["sample.urls"]  # ここにAPIのURLconfを指定する


class SwaggerView(SpectacularSwaggerView):
    pass


class RedocView(SpectacularRedocView):
    pass
