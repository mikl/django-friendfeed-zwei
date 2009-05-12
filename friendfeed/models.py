from django.db import models
from django_extensions.db.fields import UUIDField

class FriendFeedEntry(models.Model):
    """
    FriendFeed entry.

    Stores a post/tweet/whatever from FriendFeed.
    """
    id = UUIDField(primary_key=True, auto=False)
    title = models.TextField()
    link = models.URLField(verify_exists=False, blank=True, null=True)
    published = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    anonymous = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)
    service_id = models.CharField(max_length=50)
    service_name = models.CharField(max_length=150)
    service_icon_url = models.URLField(blank=True, null=True)
    service_profile_url = models.URLField(blank=True, null=True)
    user_id = UUIDField(blank=True, null=True, auto=False)
    user_nickname = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "FriendFeed entry"
        verbose_name_plural = "FriendFeed entries"

