Django Friendfeed Zwei
======================

This is a small [Django][] app that fetches and stores lifestream data from
[FriendFeed][].

It uses the friendfeed.py library provided by at [friendfeed-api][] and
stores the data fetched from FriendFeed in your local database so it
won't have to be reloaded for each pageview.

Be aware that by using FriendFeeds's API through this module, you are
bound by [their terms of service][FF-TOS].

#### What's with the name ####

Zwei means "two" in German. The reason this project is not just named
"django-friendfeed" is that there is an [earlier project by the same
name][django-friendfeed].

Django Friendfeed Zwei is not based on that code due to an incompatible
license (GPL3). The original django-friendfeed seems to have been
abandoned. At the time of this writing, the code has not been touched for
more than a year.

[Django]: http://www.djangoproject.com/ "The Django project"
[FriendFeed]: http://friendfeed.com/ "FriendFeed social networking site"
[friendfeed-api]: http://code.google.com/p/friendfeed-api/ "FriendFeed api libraries available for download"
[FF-TOS]: http://friendfeed.com/about/terms "FriendFeed Terms of Service"
[django-friendfeed]: http://code.google.com/p/django-friendfeed/ "Old django-friendfeed app"

