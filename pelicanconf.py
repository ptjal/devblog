#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tylor Allison'
SITENAME = 'Tylor Allison'
SITETITLE = AUTHOR
SITELOGO = '//s.gravatar.com/avatar/221e6e31de6232bf3175b820a4a961e7?s=120'
SITESUBTITLE = 'Game Developer'
SITEURL = 'http://127.0.0.1:8000'
THEME = "Flex"
FAVICON = '/images/favicon.ico'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True
COPYRIGHT_YEAR = 2017

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('linkedin',  'https://www.linkedin.com/in/tylor-allison'),
          ('github',    'https://github.com/tylorallison'),
          ('bitbucket', 'https://bitbucket.com/ptjal'),
          ('twitter',   'https://twitter.com/TyAllison'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "tylorallisonblog"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
