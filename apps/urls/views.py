from decouple import config
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.urls.models import ShortUrl
from apps.urls.serializers import UrlSerializer
from apps.urls.utils.generate_code import generate_code


class ShortenView(APIView):
    def post(self, request):
        serializer = UrlSerializer(data={"original_url": request.data["url"]})
        serializer.is_valid(raise_exception=True)

        url = serializer.validated_data["original_url"]

        code = generate_code(url, size=7)
        shortened_url = f'{config("DOMAIN_NAME")}/{code}'

        # Warning! This may leads to collisions as two different urls hashes can have the same first 7 characters
        # This can be addressed using a implementation with a counter where the code will always be unique

        # TODO it's linear but can be constant when we create index for short_url and original_url
        ShortUrl.objects.get_or_create(short_url=code, original_url=url)

        return Response({"short_url": shortened_url})


class GetOriginalURLView(APIView):
    def get(self, request, code):
        url = get_object_or_404(ShortUrl, short_url=code)
        return Response({"original_url": url.original_url})
