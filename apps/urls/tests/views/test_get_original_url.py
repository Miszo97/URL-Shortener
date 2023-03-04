import pytest
from rest_framework import status
from rest_framework.test import APIClient

from apps.urls.models import ShortUrl

pytestmark = pytest.mark.django_db


def test_get_original_url():
    client = APIClient()
    url = "https://www.example.com/"
    short_url = "6iY0ZL6"
    ShortUrl.objects.create(short_url=short_url, original_url=url)
    response = client.get("/6iY0ZL6", format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["original_url"] == url


def test_no_existing_short_url():
    client = APIClient()
    response = client.get("/6iY0ZL6", format="json")
    assert response.status_code == status.HTTP_404_NOT_FOUND
