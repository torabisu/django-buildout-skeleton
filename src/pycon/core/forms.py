import logging

from django import forms
from django.db.models import get_model
from django.forms import CheckboxInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button


logger = logging.getLogger(__name__)


class CheckboxLabelInput(CheckboxInput):

    def render(self, name, value, attrs=None):
        input_html = super(CheckboxLabelInput, self).render(name, value, attrs)

        return """
            <label>
                %s
                <span class="lbl"></span>
            </label>""" % input_html


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'OK'))
        self.helper.add_input(Button('cancel', 'Cancel', onclick='history.go(-1);'))
        super(BaseForm, self).__init__(*args, **kwargs)


class BaseWizardForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        super(BaseWizardForm, self).__init__(*args, **kwargs)


class BaseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.customer = None
        if 'customer' in kwargs:
            logger.debug('Customer passed into form...')
            self.customer = kwargs.pop('customer')
            logger.debug('self.customer = %s' % self.customer)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'OK'))
        self.helper.add_input(Button('cancel', 'Cancel', onclick='history.go(-1);'))

        super(BaseModelForm, self).__init__(*args, **kwargs)

        if self.customer:
            logger.debug('fields.customer = %s' % self.customer)

            self.fields['customer'].initial = self.customer
            self.fields['customer'].widget = forms.HiddenInput()
