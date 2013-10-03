import time
import logging
import random

from celery import task


logger = logging.getLogger(__name__)


@task(ignore_result=True)
def make_wine():
    seconds = random.randint(1, 5)
    logger.info('Making wine for %d seconds...' % seconds)
    time.sleep(seconds)
