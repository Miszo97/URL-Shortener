from urllib.parse import urlparse

from decouple import config
from django.core.validators import URLValidator
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from apps.urls.models import ShortUrl


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ["original_url"]

    def validate_original_url(self, value):
        parsed_url = urlparse(value)
        domain_name = parsed_url.netloc.split(":")[0]
        if domain_name == config("DOMAIN_NAME"):
            raise ValidationError("This domain is not allowed.")

        return value
