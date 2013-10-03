import re
import logging
from datetime import date, timedelta
from dateutil import relativedelta


logger = logging.getLogger(__name__)


def camel_to_underscore(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def sync_objects(source_object, target_object, fields):
    """
    Runs through all the fields, and compares them to the source and
    the target object.  If the values don't match, the target object's field
    is updated.
    """
    updated = False

    for source_field, target_field in fields.iteritems():

        if hasattr(source_object, source_field) and hasattr(target_object, target_field) \
            and getattr(source_object, source_field) != getattr(target_object, target_field):

            setattr(target_object, target_field, getattr(source_object, source_field))
            updated = True

    return target_object, updated


def delete_objects(source_objects, target_objects, source_pkey='id', target_pkey='id'):
    logger.info('Checking if target objects need to be deleted...')
    for object in target_objects:
        logger.debug('%s exists, checking source...' % object)
        kwargs = {source_pkey: getattr(object, target_pkey)}
        logger.debug('kwargs = %s' % kwargs)
        try:
            source_objects.filter(**kwargs)[0]
        except IndexError:
            logger.warning('Deleting %s...' % object)
            object.delete()


def __check_number(digits):
    _sum = 0
    alt = False
    for d in reversed(digits):
        d = int(d)
        assert 0 <= d <= 9
        if alt:
            d *= 2
            if d > 9:
                d -= 9
        _sum += d
        alt = not alt
    return (_sum % 10) == 0


def generate_check_digit(number):
    data = '%06d' % number
    for counter in range(0, 10):
        if __check_number(data + str(counter)):
            return '%s-%d' % (data, counter)


def is_true(value):
    if str(value) in ['True', 'true', '1', 't', 'T' 'y', 'yes', 'Yes']:
        return True
    else:
        return False


def module_import(name):
    """
    If you need to import a module on the fly, this helper function assists
    you.  So say you want to import something like spam.eggs.are.cool, this
    will sort out the full import.
    """
    mod = __import__(name, globals(), locals(), [], -1)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod