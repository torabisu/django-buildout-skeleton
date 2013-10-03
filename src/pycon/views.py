import logging

from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse


logger = logging.getLogger(__name__)


def index(request, template='pycon/index.html'):
    return TemplateResponse(request, template)
