from currency.models import Banks, ContactUs, Rate
from crispy_forms.helper import FormHelper

from django import forms


class BankForm(forms.ModelForm):
    class Meta:
        model = Banks
        fields = (
            'name',
            'url',
            'email_from',
            'number_phone'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'type',
            'sale',
            'buy',
            'bank',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
