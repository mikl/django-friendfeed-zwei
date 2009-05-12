import logging
from django.core.management.base import NoArgsCommand, CommandError
from django.conf import settings
import friendfeed.friendfeed
from friendfeed.models import FriendFeedEntry

class Command(NoArgsCommand):
    help = "Fetch items from FriendFeed, updating our local cache."

    def handle_noargs(self, **options):
        """ Fetch data from FriendFeed and store it in the database. """
        if not hasattr(settings, 'FRIENDFEED_USERS') or not settings.FRIENDFEED_USERS:
            raise CommandError("This command requires FRIENDFEED_USERS to be set in settings.py. It should be a list or tuple with one or more FriendFeed usernames.")

        log = logging.getLogger('friendfeed')
        service = friendfeed.friendfeed.FriendFeed()

        # If there is only one user, just fetch that.
        if len(settings.FRIENDFEED_USERS) == 1:
            feed = service.fetch_user_feed(settings.FRIENDFEED_USERS[0])
        # Otherwise, use the multi user feed.
        else:
            feed = service.fetch_multi_user_feed(settings.FRIENDFEED_USERS)

        for data in feed['entries']:
            try:
                entry = FriendFeedEntry.objects.get(pk=data['id'])
            except FriendFeedEntry.DoesNotExist:
                log.debug('Could not find existing FriendFeedEntry %s.' % data['id'])
                entry = FriendFeedEntry()
                entry.id = data['id']
                entry.new = True

            if hasattr(entry, 'new') or entry.updated < data['updated']:
                entry.title = data['title']
                entry.link = data['link']
                entry.published = data['published']
                entry.updated = data['updated']
                entry.anonymous = data['anonymous']
                entry.hidden = data['hidden']
                entry.service_id = data['service']['id']
                entry.service_name = data['service']['name']
                entry.service_icon_url = data['service']['iconUrl']
                entry.service_profile_url = data['service']['profileUrl']
                entry.user_id = data['user']['id']
                entry.user_nickname = data['user']['nickname']
                entry.save()
                log.debug('Wrote new data to FriendFeedEntry %s.' % entry.id)
            else:
                log.debug('Not updating FriendFeedEntry %s.' % data['id'])

