import os
from unittest import mock

import pytest
from rest_framework import status
from rest_framework.test import APIClient

from apps.urls.models import ShortUrl

pytestmark = pytest.mark.django_db


def test_shorten_valid_url():
    client = APIClient()
    url = "https://www.example.com/"
    response = client.post("/shorten/", {"url": url}, format="json")

    assert response.status_code == status.HTTP_200_OK

    created_url = ShortUrl.objects.all()[0]
    assert created_url.original_url == url


def test_shorten_invalid_url():
    client = APIClient()
    response = client.post("/shorten/", {"url": "not_a_url"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@mock.patch.dict(os.environ, {"DOMAIN_NAME": "www.example.com"})
def test_user_shortens_service_domain_name():
    client = APIClient()
    response = client.post("/shorten/", {"url": "https://www.example.com/"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_same_url_always_shortened_to_same_code():
    client = APIClient()

    response_1 = client.post("/shorten/", {"url": "https://www.example.com/"})
    assert response_1.status_code == status.HTTP_200_OK

    response_2 = client.post("/shorten/", {"url": "https://www.example.com/"})
    assert response_2.status_code == status.HTTP_200_OK

    assert response_1.data == response_2.data
    assert ShortUrl.objects.count() == 1


def test_different_urls_shortened_to_different_codes():
    client = APIClient()

    response_1 = client.post("/shorten/", {"url": "https://www.example.com/"})
    assert response_1.status_code == status.HTTP_200_OK

    response_2 = client.post("/shorten/", {"url": "https://www.example1.com/"})
    assert response_1.status_code == status.HTTP_200_OK

    assert response_1.data != response_2.data
    assert ShortUrl.objects.count() == 2
