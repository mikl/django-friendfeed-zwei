from django.contrib import admin
from models import FriendFeedEntry

class FriendFeedEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'published'
    list_display = ('published', 'service_name', 'title')
    list_filter = ('service_name', 'published')
    ordering = ('-published',)

admin.site.register(FriendFeedEntry, FriendFeedEntryAdmin)

