from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from pycon.auth.models import EndUser
from pycon.auth.forms import EndUserForm


@login_required
def users_profile(request, profile_id, template_name='pycon/auth/users/profile.html'):
    end_user = EndUser.objects.get(id=profile_id)
    return TemplateResponse(request, template_name, {'end_user': end_user})


@login_required
def users_edit(request, template_name='pycon/auth/users/edit.html'):
    if request.method == 'POST':
        form = EndUserForm(instance=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/auth/users/view/')
    else:
        form = EndUserForm(instance=request.user)
    return TemplateResponse(request, template_name, {'end_user': request.user, 'form': form})
