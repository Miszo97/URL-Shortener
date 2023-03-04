from django.db import models


class ShortUrl(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url} to {self.short_url}"
