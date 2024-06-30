AUTHOR = 'Benoit Boyadjis'
SITEURL = "" # "https://bboyadjis.github.io/mariage-rosalie-benoit"
PATH = "content"

SITENAME = 'Mariage Rosalie et Benoit'
SITETITLE = 'Mariage Rosalie et Benoit'
TAG_LINE = "Paris, 20 Juillet 2024"
SITESUBTITLE = "Paris, 20 Juillet 2024"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Programme du Samedi", "programme-samedi"),
    ("Programme du Dimanche", "programme-dimanche"),
    ("Liste de Mariage", "liste-mariage"),
    ("Contacts", "contacts"),
    ("F.A.Q.", "faq"),
)

# Social widget
SOCIAL = ()

STATIC_PATHS = [
    'images',
]
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'}, 
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "/home/ben/anaconda3/envs/pelican/lib/python3.12/site-packages/pelican/themes/Flex"