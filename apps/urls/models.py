from django.db import models


class ShortUrl(models.Model):
    # We can think about indexing here to speed up objects queries but we should keep in mind that
    # while indexing can improve query performance, it can also have a negative impact on write performance and database size.
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # as a feature, we can also add an expiration date here

    def __str__(self):
        return f"{self.original_url} to {self.short_url}"
