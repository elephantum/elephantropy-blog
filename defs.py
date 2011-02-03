# $Id$

import os

def _get_on_gae():
    _server_software = os.environ.get('SERVER_SOFTWARE','').lower()
    if _server_software.startswith('goog'):
        return True
    else:
        return False

# TODO cleanup these defs
ON_GAE = _get_on_gae()
PROD_MODE = ON_GAE
DEV_MODE = not ON_GAE

###

CANONICAL_BLOG_URL = 'http://blog.elephantropy.com'  
    
BLOG_NAME = 'Elephantropy Blog'
BLOG_OWNER = 'Andrey Tatarinov'

TEMPLATE_SUBDIR = 'templates'

TAG_URL_PATH = 'tag'
DATE_URL_PATH = 'date'
ARTICLE_URL_PATH = 'article'
MEDIA_URL_PATH = 'static'
ATOM_URL_PATH = 'atom'
RSS2_URL_PATH = 'rss2'
ARCHIVE_URL_PATH = 'archive'

MAX_ARTICLES_PER_PAGE = 5
TOTAL_RECENT = 10

### Google Analytics

GA_KEY = 'UA-18937217-3'
# GA_KEY = 'UA-18937217-2' # elephantropy-blog.appspot.com

### Disqus comments

DISQUS = True
DISQUS_SHORTNAME = 'elephantropy-blog-appspot-com'

###

PING_TECHNORATI = False
TECHNORATI_PING_RPC_URL = 'http://rpc.technorati.com/rpc/ping'
FAKE_TECHNORATI_PING_RPC_URL = 'http://localhost/~bmc/technorati-mock/'
