from base import *
import dj_database_url

DEBUG = False
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environmental variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_J4IZwyrMGBHuK19n0wOE9bqJ')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_TPPuCVTkDLuLNqhDzsmxi4AM')

# Disqus
DISQUS_API_KEY = 'wu9qhvYBAn9nWquS1jTOxjgpb8P43gYWkmvfsHpC6lMJEIwnZkNNrIdr5nhWOZ46'
DISQUS_WEBSITE_SHORTNAME = 'pchobbyistblog'

SITE_URL = "https://the-pc-hobbyist.herokuapp.com"
ALLOWED_HOSTS.append('the-pc-hobbyist.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}