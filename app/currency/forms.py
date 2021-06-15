from currency.models import Banks, ContactUs

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
