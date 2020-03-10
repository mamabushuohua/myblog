from .common import *


SECRET_KEY = 'development-secret-key'

DEBUG = True

print('local')

ALLOWED_HOSTS = ['*']

# 搜索设置
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://elasticsearch_local:9200/'
