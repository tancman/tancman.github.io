#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from slugify import slugify

AUTHOR = u'Tancman'
AUTHOR_EMAIL = u'atendimento@tancman.com.br'
AUTHOR_PHONE = u'(21) 98352-4442'
AUTHOR_ADDRESS = u'Vargem Grande<br>Rio de Janeiro'
AUTHOR_MAPS = u'https://www.google.com.br/maps/place/R.+Manhua%C3%A7u+-+Vargem+Grande,+Rio+de+Janeiro+-+RJ/@-22.9810134,-43.4972055,17z/data=!3m1!4b1!4m5!3m4!1s0x9be7906db9a8c3:0x50b9b9d955b5aff2!8m2!3d-22.9810134!4d-43.4950168?hl=pt-br'
AUTHOR_MAPS_EMBED = u'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3673.163528563044!2d-43.49720548503303!3d-22.9810133849741!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9be7906db9a8c3%3A0x50b9b9d955b5aff2!2sR.+Manhua%C3%A7u+-+Vargem+Grande%2C+Rio+de+Janeiro+-+RJ!5e0!3m2!1spt-BR!2sbr!4v1469383607808"'

SITENAME = u'tancman'
SITEURL = u'http://tancman.com.br'
SITELOGO = u'/images/common/logo.jpg'
FAVICON = u'/images/common/favicon.png'
SITELOGO_SIZE = u'20px'
HIDE_SITENAME = False
CUSTOM_CSS = u'css/global.css'

GITHUB_URL = u'https://github.com/tancman'
TWITTER_URL = u'https://twitter.com/tancmanbr'
FACEBOOK_URL = u'https://facebook.com/tancmanbr'
LINKEDIN_URL = u'https://www.linkedin.com/company/tancman'
DISQUS_SITENAME = u'tancman'
ADDTHIS_PROFILE = u'tancman'

BANNER_TITLE = u'tancman'
BANNER_SUBTITLE = u'Desenvolvimento de Software'
BANNER_IMG = u'/images/common/banner.jpg'
BANNER_LINK = u'#about'
DEFAULT_BANNER_LINK = u'#rtc-content'
BANNER_LINK_LABEL = u'Saiba Mais'
DEFAULT_BANNER_LINK_LABEL = u'Ir para o conteúdo'
BANNER_LOGO = u'/images/common/logo.jpg'

ABOUT_ME = u'Tancman Consultoria em Desenvolvimento de Software tem como missão geração de valor para os seus clientes utilizando software como meio para realizar projetos.'
ABOUT_ME_RECOMENDS = False
ABOUT_ME_RECOMENDS_LIST = []

GOOGLE_ANALYTICS = ''
FACEBOOK_APPID = ''
GOOGLE_TAGMANAGER = ''

# Articles
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISQUS_DISPLAY_COUNTS = True

# Caregories
CATEGORY_BANNER_IMG = u'/images/common/banner.jpg'
CATEGORY_BANNER_SUBTITLE = u'Veja todos os posts desta categoria.'

TIMEZONE = 'America/Sao_Paulo'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/rtancman'),
    ('twitter', 'https://twitter.com/rtancman'),
    ('rss', 'feeds/all.atom.xml'),
)

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Plugins
PLUGIN_PATHS = [
    'pelican-plugins',
    # 'custom-plugins'
]

PLUGINS = [
    'gravatar',
    # 'pelican_alias', # para criar alias para artigos
    'sitemap',
    'pelican_youtube',  # funciona somente com arquivos rst
    'pelican_vimeo',  # funciona somente com arquivos rst
    # 'json_articles',
    'gzip_cache'  # deve ser o ultimo plugin
    # 'pdf', # funciona somente com arquivos rst

]

DEFAULT_PAGINATION = 10

# Theme
THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Geracao de PDF
# PDF_GENERATOR = True


def makeimgbanner(category=''):
    return '/images/categories/' + slugify(str(category)) + '.jpg'


JINJA_FILTERS = {'imgbanner':makeimgbanner}