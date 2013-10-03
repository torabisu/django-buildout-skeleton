import logging
from datetime import date, timedelta
from copy import deepcopy
from dateutil import relativedelta
from polymorphic import PolymorphicModel

from django.db import models


logger = logging.getLogger(__name__)


class Base(PolymorphicModel):
    """
    If your class needs the basics, like created date, modified date etc, then inherit from this Base class.
    """
    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s [%s]' % (self.__class__.__name__, self.id)

    def class_name(self):
        return str(self.__class__.__name__).lower()

    def to_json(self, include_related=True):
        return {
            'id': self.id,
            'created': self.created.isoformat(),
            'modified': self.modified.isoformat(),
            'class_name': self.__class__.__name__
        }

    def cast(self):
        """
        This method is quite handy, it converts "self" into its correct child class. For example:

        .. code-block:: python

           class Fruit(models.Model):
               name = models.CharField()

           class Apple(Fruit):
               pass

           fruit = Fruit.objects.get(name='Granny Smith')
           apple = fruit.cast()

        :return self: A casted child class of self
        """
        logger.debug('Checking if we can cast %s to a child class...' % self.__class__.__name__)

        for name in dir(self):
            if '_ptr' not in name:
                try:
                    attr = getattr(self, name)
                    if isinstance(attr, self.__class__) and attr.__class__.__name__ != self.__class__.__name__:
                        return attr.cast()
                except:
                    pass
        return self


class BaseFolder(Base):
    ext_id = models.CharField(max_length=16, unique=True, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=128)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    @property
    def children(self):
        return self.__class__.objects.filter(parent=self)

    def display(self, level=1, h_level=1):
        setattr(self, 'level', level)
        setattr(self, 'h_level', h_level)
        records = [self]
        for child in self.children:
            records.extend(child.display(level + 1, h_level + 1))
        return records


class ListQuerySet(models.query.EmptyQuerySet):

    def __init__(self, model=None, query=None, using=None):
        super(ListQuerySet, self).__init__(model, query, using)
        self._result_cache = []

    def __and__(self, other):
        return self._clone()

    def __or__(self, other):
        return other._clone()

    def count(self):
        return len(self._result_cache)

    def delete(self):
        pass

    def _clone(self, klass=None, setup=False, **kwargs):
        c = super(ListQuerySet, self)._clone(klass, setup=setup, **kwargs)
        c._result_cache = deepcopy(self._result_cache)
        return c

    def append(self, entry):
        self._result_cache.append(entry)

    def extend(self, list):
        self._result_cache.extend(list)

    def iterator(self):
        # This slightly odd construction is because we need an empty generator
        # (it raises StopIteration immediately).
        yield iter(self._result_cache).next()

    def all(self):  # @ReservedAssignment
        return self._result_cache

    def filter(self, *args, **kwargs):  # @ReservedAssignment
        obj = self._clone()
        obj._result_cache = []
        dataset = self._result_cache
        for k, v in kwargs.iteritems():
            name = k.split('__')[0]
            for item in dataset:
                if item.has_key(name) and v in str(item[name]):
                    obj._result_cache.append(item)
                else:
                    dataset.remove(item)

        return obj

    def exclude(self, *args, **kwargs):
        return self._result_cache

    def complex_filter(self, filter_obj):
        return self._result_cache

    def select_related(self, *fields, **kwargs):
        return self._result_cache

    def annotate(self, *args, **kwargs):
        return self._result_cache

    def order_by(self, *field_names):
        obj = self._clone()

        try:
            logger.debug('field_names = %s' % str(field_names))
            field = str(field_names[0])
            if '-' in field:
                reverse = True
                sort_on = field.replace('-', '')
            else:
                reverse = False
                sort_on = field.replace('-', '')

            decorated = [(dict_[sort_on], dict_) for dict_ in self._result_cache]
            if reverse:
                decorated.reverse()
            else:
                decorated.sort()
            obj._result_cache = [dict_ for (key, dict_) in decorated]  # @UnusedVariable
            return obj
        except Exception, ex:
            logger.fatal(ex)
            return self

    def distinct(self, true_or_false=True):
        return self._result_cache

    def extra(self, select=None, where=None, params=None, tables=None,
              order_by=None, select_params=None):
        assert self.query.can_filter(), \
                "Cannot change a query once a slice has been taken"
        return self

    def reverse(self):
        return self._result_cache

    def defer(self, *fields):
        return self._result_cache

    def only(self, *fields):
        return self._result_cache

    def update(self, **kwargs):
        """
        Don't update anything.
        """
        return 0


class Period(object):

    def __init__(self, number=0, billing_day=25):

        try:
            self.number = int(number)
        except:
            self.number = 0

        now = date.today()
        start = date(now.year, now.month, 1)

        if self.number < 0:
            months_back = self.number * -1
            start = start - relativedelta.relativedelta(months=months_back)
            end = start + relativedelta.relativedelta(months=1)
        else:
            end = now

        if end - start <= timedelta(days=1):
            interval = '5min'
        elif end - start <= timedelta(days=20):
            interval = 'hourly'
        elif end - start <= timedelta(days=90):
            interval = 'daily'
        else:
            interval = 'monthly'

        self.start = start
        self.end = end
        self.interval = interval
        self.prev_number = self.number - 1
        self.next_number = self.number + 1
        self.month = self.start.strftime('%B, %Y')
        self.billing_day = billing_day
        self.billing_end = date(self.start.year, self.start.month, self.billing_day)
        self.billing_start = self.billing_end - relativedelta.relativedelta(months=1)
        logger.debug('self.start = %s' % self.start)
        logger.debug('self.end = %s' % self.end)