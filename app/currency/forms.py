from currency.models import Banks, ContactUs, Rate

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


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message'
        )


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'type',
            'sale',
            'buy',
            'source'
        )
