from django.urls import path, re_path

from apps.urls.views import GetOriginalURLView, ShortenView

urlpatterns = [
    path("shorten/", ShortenView.as_view()),
    # regex to get 7 character long alphanumeric characters
    re_path(r"^(?P<code>[a-zA-Z0-9]{7})$", GetOriginalURLView.as_view()),
]
