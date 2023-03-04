from urllib.parse import urlparse

from decouple import config
from django.core.validators import URLValidator
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class UrlSerializer(serializers.Serializer):
    url = serializers.CharField(required=True, validators=[URLValidator()])

    def validate_url(self, value):
        parsed_url = urlparse(value)
        domain_name = parsed_url.netloc.split(":")[0]
        if domain_name == config("DOMAIN_NAME"):
            raise ValidationError("This URL is not allowed.")

        return value
