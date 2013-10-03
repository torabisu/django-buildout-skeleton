import json
import logging

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import FieldError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.response import TemplateResponse


logger = logging.getLogger(__name__)


def _format_filter(filter_criteria):
    formatted_filters = {}
    try:
        user_defined_filter = json.loads(filter_criteria)
        for field_name, value in user_defined_filter.iteritems():
            search_field = str(field_name).replace('.', '__')
            key = search_field + '__icontains'
            formatted_filters[key] = value
    except Exception, ex:
        logger.critical('Hit exception on filter %s' % ex)
    return formatted_filters


@login_required
def _list_view(request, object_list, template=None, additional_fields={}, filter=''):
    """
    List view is not called directly from core, its used in other views to
    handle the tables or lists of objects like assets, devices, jobs etc.

    .. note:: There's a little bit of magic around when you want to refresh
        the table data only as the base_template gets overridden.

    :param request: The HttpRequest with the following attributes:

        * page_size: How many rows to show
        * page: Current page that you're on
        * sort_field: The Django field to sort by
        * sort_direction: True if you wish to which to sort descending
        * filter: we get a json string of a dict defining
        * search_text: The free-text that the user typed in to search on
        * data_only: Set to True if only the table data is to be returned

    :param object_list: A list of objects (Django queryset)
    :param template: The name of the template, used in TemplateResponse
    :param additional_fields: A dictionary of any additional fields you want to pass to the
        template.

    :return TemplateResponse:
    """
    page_size = getattr(settings, 'PAGE_SIZE', 25)
    page = request.REQUEST.get('page', 1)
    sort_field = request.REQUEST.get('sort_field', False)
    sort_direction = request.REQUEST.get('sort_direction', 'asc')
    sort_index = request.REQUEST.get('sort_index', -1)
    filter = request.REQUEST.get('filter', filter)

    if filter:
        formatted_filters = _format_filter(filter)
        try:
            object_list = object_list.filter(**formatted_filters)
        except FieldError:
            logger.warning('Could not search on fields %s' % formatted_filters)

    if sort_field:
        try:
            sort_field = str(sort_field).replace('.', '__')
            if sort_direction.lower() == 'desc':
                sort = '-' + sort_field
            else:
                sort = sort_field
            logger.debug('Sorting by %s...' % sort)
            object_list = object_list.order_by(sort)
        except FieldError:
            logger.warning('Could not sort on field %s' % sort_field)

    paginator = Paginator(object_list, page_size)
    logger.debug('paginator = %s' % paginator)
    logger.debug('paginator.num_pages = %s' % paginator.num_pages)
    logger.debug('paginator total items = %s' % paginator.count)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    start = queryset.number - 3
    if start < 1:
        start = 0
        end = 5
    else:
        end = queryset.number + 2

    if end > queryset.paginator.num_pages:
        end = queryset.paginator.num_pages
        start = queryset.paginator.num_pages - 5
        if start < 1:
            start = 0

    page_range = paginator.page_range[start:end]

    logger.debug('page_range = %s' % page_range)

    fields = {
        'queryset': queryset,
        'page_range': page_range,
        'sort_direction': sort_direction,
        'sort_index': sort_index,
        'filter': filter
    }

    fields.update(additional_fields)

    if not template:
        return queryset

    return TemplateResponse(request, template, fields)