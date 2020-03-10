from .common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

print('production')
DEBUG = False

ALLOWED_HOSTS = ['blog.liequantech.com']
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://hellodjango_blog_tutorial_elasticsearch:9200/'
