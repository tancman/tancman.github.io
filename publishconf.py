#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = ""

# TEMPLATE_PAGES = {
#     os.path.join(BASE, 'theme/templates/search.html'): os.path.join(BASE, 'output/pages/search.html')
# }