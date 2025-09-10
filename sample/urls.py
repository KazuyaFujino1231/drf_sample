from django.contrib import admin
from django.urls import path

from .view import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user', views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/tweet', views.TweetViewSet.as_view({'get': 'list', 'post':'create'})),
]

