from pycon.core.forms import BaseModelForm

from pycon.auth.models import EndUser


class EndUserForm(BaseModelForm):

    class Meta:
        model = EndUser
