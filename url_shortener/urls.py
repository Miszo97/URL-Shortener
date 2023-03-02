from django.urls import path

from apps.urls.views import HelloWorld

urlpatterns = [path("shorten/", HelloWorld.as_view())]
