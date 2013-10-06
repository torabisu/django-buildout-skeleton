import logging

from django.conf.urls import patterns, url, include
from django.conf import settings

from rest_framework import routers
from rest_framework.viewsets import ViewSet

from pycon.core.utils import module_import


logger = logging.getLogger(__name__)
logger.debug('Setting up API authentication...')

router = routers.DefaultRouter()
router.include_format_suffixes = True

urlpatterns = patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)

for app in settings.INSTALLED_APPS:

    try:
        module = module_import('%s.api' % app)
        logger.debug('Importing %s.api...' % app)

        for member in dir(module):
            if isinstance(member, ViewSet):
                logger.info('member = %s' % member)
                ViewSet = getattr(module, member)
                name = member.replace('ViewSet', '').lower()
                api_url = app.split('.')[-1] + '/' + name
                logger.debug('api_url = %s' % api_url)
                router.register(api_url, ViewSet)

    except ImportError:
        logger.debug('%s.api does not exist...\n' % app)


urlpatterns += url(r'^', include(router.urls)),
