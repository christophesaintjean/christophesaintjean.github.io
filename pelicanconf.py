#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Christophe Saint-Jean'
LIBRAVATAR_AUTHOR_EMAIL ='christophe.saint-jean@univ-lr.fr'
SITENAME = 'Homepage of Christophe Saint-Jean'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
#RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('MIA Lab.', 'http://mia.univ-larochelle.fr/'),
         ('CS Dep.', 'https://sciences.univ-larochelle.fr/departement-d-informatique'),
         ('La Rochelle University', 'https://www.univ-larochelle.fr/'),
         ('Féderation de Recherche MIRES', 'http://mires.prd.fr/'),)

TWITTER_USERNAME='CSJ_ULR'

# Social widget
SOCIAL = (('@' + TWITTER_USERNAME, 'https://twitter.com/CSJ_ULR'),
          ('Profile on LinkedIn', 'http://fr.linkedin.com/pub/christophe-saint-jean/22/89b/793'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'notebooks']

THEME = 'notmyidea'
#THEME_PRIMARY = "blue"
#THEME_ACCENT = "amber"

PLUGIN_PATHS = ['plugins']
PLUGINS = ['libravatar', 'render_math', 'pelican_youtube']

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ("Home", "/pages/contact.html"),
    ("Blog", "/index.html"),
    ("Research", "/pages/research.html"),
    ("Publications", "/pages/publications.html"),
    ("Software", "/pages/software.html"),
    ("Tags", "/tweets.html"),
]

DISCLAIMER = False
COPYRIGHT = False





