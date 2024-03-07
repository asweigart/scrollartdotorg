AUTHOR = 'Al Sweigart'
SITENAME = 'The Scroll Art Museum'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    #("Pelican", "https://getpelican.com/"),
    #("Python.org", "https://www.python.org/"),
    #("Jinja2", "https://palletsprojects.com/p/jinja/"),
    #("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    #("You can add links in your config file", "#"),
    #("Another social link", "#"),
)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'basic'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

FILENAME_METADATA = '(?P<slug>.*?)\\.html'
OUTPUT_PATH = '../output'
FAVICON = '../favicon.ico'
SITESUBTITLE = 'Exhibits of scrolling animated ASCII art.'
DEFAULT_CATEGORY = 'Scroll Art Exhibits'
STATIC_PATHS = ['static']

PAGE_EXCLUDES = ['static']
ARTICLE_EXCLUDES = ['static']


