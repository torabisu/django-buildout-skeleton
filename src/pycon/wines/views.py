import logging

from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse


from pycon.wines.models import WhiteWine, RedWine
from pycon._wordpress.models import Post

logger = logging.getLogger(__name__)


def white_wines_list(request, template='pycon/wines/white_wines/list.html'):
    white_wines = WhiteWine.objects.all()
    return TemplateResponse(request, template, {'white_wines': white_wines})


@login_required
def red_wines_list(request, template='pycon/wines/red_wines/list.html'):
    red_wines = RedWine.objects.all()
    return TemplateResponse(request, template, {'red_wines': red_wines})


def posts_list(request, template='pycon/wines/posts/list.html'):
    posts = Post.objects.all()[0:20]
    return TemplateResponse(request, template, {'posts': posts})

